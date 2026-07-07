from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.gitlab_client import GitLabClient
from app.models import Issue, MergeRequest, Pipeline, Repository
from app.schemas import RepositoryResponse

router = APIRouter(prefix="/repository", tags=["repository"])


def _client() -> GitLabClient:
    if not settings.gitlab_token:
        raise HTTPException(400, "GITLAB_TOKEN non configuré")
    return GitLabClient(settings.gitlab_url, settings.gitlab_token)


@router.get("/{project_id}", response_model=RepositoryResponse)
async def get_repository(project_id: int, db: Session = Depends(get_db)):
    repo = db.query(Repository).filter(Repository.gitlab_id == project_id).first()
    if not repo:
        raise HTTPException(404, "Dépôt non trouvé")
    return repo


@router.post("/{project_id}/sync")
async def sync_repository(project_id: int, db: Session = Depends(get_db)):
    client = _client()
    data = await client.get_project(project_id)

    repo = db.query(Repository).filter(Repository.gitlab_id == project_id).first()
    if repo:
        repo.name = data["name"]
        repo.description = data.get("description", "")
        repo.default_branch = data.get("default_branch", "main")
    else:
        repo = Repository(
            gitlab_id=project_id,
            name=data["name"],
            description=data.get("description", ""),
            default_branch=data.get("default_branch", "main"),
        )
        db.add(repo)

    db.commit()
    db.refresh(repo)
    return {"status": "synchronisé", "repository_id": repo.id}


@router.get("/{project_id}/stats")
async def get_stats(project_id: int, db: Session = Depends(get_db)):
    mrs = db.query(func.count(MergeRequest.id)).filter(
        MergeRequest.project_id == project_id, MergeRequest.state == "opened"
    ).scalar() or 0

    issues = db.query(func.count(Issue.id)).filter(
        Issue.project_id == project_id, Issue.state == "opened"
    ).scalar() or 0

    pipelines = db.query(func.count(Pipeline.id)).filter(
        Pipeline.project_id == project_id
    ).scalar() or 0

    return {
        "project_id": project_id,
        "open_merge_requests": mrs,
        "open_issues": issues,
        "pipelines": pipelines,
    }
