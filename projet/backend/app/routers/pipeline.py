from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.gitlab_client import GitLabClient
from app.models import Pipeline
from app.schemas import PipelineResponse

router = APIRouter(prefix="/pipelines", tags=["pipelines"])


def _client() -> GitLabClient:
    if not settings.gitlab_token:
        raise HTTPException(400, "GITLAB_TOKEN non configuré")
    return GitLabClient(settings.gitlab_url, settings.gitlab_token)


@router.get("/{project_id}", response_model=list[PipelineResponse])
async def get_pipelines(project_id: int, db: Session = Depends(get_db)):
    return (
        db.query(Pipeline)
        .filter(Pipeline.project_id == project_id)
        .order_by(Pipeline.created_at.desc())
        .all()
    )


@router.post("/{project_id}/sync", response_model=list[PipelineResponse])
async def sync_pipelines(project_id: int, db: Session = Depends(get_db)):
    client = _client()
    data = await client.get_pipelines(project_id)

    db.query(Pipeline).filter(Pipeline.project_id == project_id).delete()

    now = datetime.utcnow()
    for pipeline in data:
        db.add(
            Pipeline(
                gitlab_id=pipeline["id"],
                project_id=project_id,
                status=pipeline["status"],
                duration=pipeline.get("duration"),
                branch=pipeline.get("ref", "main"),
                created_at=now,
            )
        )

    db.commit()
    return (
        db.query(Pipeline)
        .filter(Pipeline.project_id == project_id)
        .order_by(Pipeline.created_at.desc())
        .all()
    )
