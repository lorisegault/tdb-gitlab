from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.gitlab_client import GitLabClient
from app.models import MergeRequest
from app.schemas import MergeRequestResponse

router = APIRouter(prefix="/merge-requests", tags=["merge_requests"])


def _client() -> GitLabClient:
    if not settings.gitlab_token:
        raise HTTPException(400, "GITLAB_TOKEN non configuré")
    return GitLabClient(settings.gitlab_url, settings.gitlab_token)


@router.get("/{project_id}", response_model=list[MergeRequestResponse])
async def get_merge_requests(project_id: int, db: Session = Depends(get_db)):
    return (
        db.query(MergeRequest)
        .filter(
            MergeRequest.project_id == project_id,
            MergeRequest.state == "opened",
        )
        .all()
    )


@router.post("/{project_id}/sync", response_model=list[MergeRequestResponse])
async def sync_merge_requests(project_id: int, db: Session = Depends(get_db)):
    client = _client()
    data = await client.get_merge_requests(project_id)

    db.query(MergeRequest).filter(MergeRequest.project_id == project_id).delete()

    for mr in data:
        author = mr.get("author", {})
        author_name = author.get("name", "") if isinstance(author, dict) else str(author)
        db.add(
            MergeRequest(
                gitlab_id=mr["id"],
                project_id=project_id,
                title=mr["title"],
                author=author_name,
                state=mr["state"],
                comments_count=mr.get("user_notes_count", 0),
                approvals_count=mr.get("approvals_count", 0),
            )
        )

    db.commit()
    return (
        db.query(MergeRequest)
        .filter(
            MergeRequest.project_id == project_id,
            MergeRequest.state == "opened",
        )
        .all()
    )
