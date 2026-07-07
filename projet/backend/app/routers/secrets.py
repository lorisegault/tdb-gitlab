from fastapi import APIRouter, Depends, HTTPException

from app.config import settings
from app.gitlab_client import GitLabClient

router = APIRouter(prefix="/secrets", tags=["secrets"])


def _client() -> GitLabClient:
    if not settings.gitlab_token:
        raise HTTPException(400, "GITLAB_TOKEN non configuré")
    return GitLabClient(settings.gitlab_url, settings.gitlab_token)


@router.get("/{project_id}")
async def get_secrets(project_id: int):
    client = _client()
    variables = await client.get_variables(project_id)
    return {"variables": variables}
