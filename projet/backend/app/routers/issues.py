from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.gitlab_client import GitLabClient
from app.models import Issue
from app.schemas import IssueResponse

router = APIRouter(prefix="/issues", tags=["issues"])


def _client() -> GitLabClient:
    if not settings.gitlab_token:
        raise HTTPException(400, "GITLAB_TOKEN non configuré")
    return GitLabClient(settings.gitlab_url, settings.gitlab_token)


@router.get("/{project_id}", response_model=list[IssueResponse])
async def get_issues(project_id: int, db: Session = Depends(get_db)):
    return (
        db.query(Issue)
        .filter(
            Issue.project_id == project_id,
            Issue.state == "opened",
        )
        .all()
    )


@router.post("/{project_id}/sync", response_model=list[IssueResponse])
async def sync_issues(project_id: int, db: Session = Depends(get_db)):
    client = _client()
    data = await client.get_issues(project_id)

    db.query(Issue).filter(Issue.project_id == project_id).delete()

    now = datetime.utcnow()
    for issue in data:
        author = issue.get("author", {})
        author_name = author.get("name", "") if isinstance(author, dict) else str(author)

        labels = issue.get("labels", [])
        labels_str = ",".join(labels) if isinstance(labels, list) else str(labels)

        assignee = issue.get("assignee")
        assignee_name = None
        if assignee and isinstance(assignee, dict):
            assignee_name = assignee.get("name")

        due_date = issue.get("due_date")
        if due_date:
            due_date = datetime.fromisoformat(due_date)

        db.add(
            Issue(
                gitlab_id=issue["id"],
                project_id=project_id,
                title=issue["title"],
                author=author_name,
                state=issue["state"],
                labels=labels_str,
                assignee=assignee_name,
                due_date=due_date,
                created_at=now,
            )
        )

    db.commit()
    return (
        db.query(Issue)
        .filter(
            Issue.project_id == project_id,
            Issue.state == "opened",
        )
        .all()
    )
