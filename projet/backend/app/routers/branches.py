from fastapi import APIRouter, Depends, HTTPException

from app.config import settings
from app.gitlab_client import GitLabClient

router = APIRouter(prefix="/branches", tags=["branches"])


def _client() -> GitLabClient:
    if not settings.gitlab_token:
        raise HTTPException(400, "GITLAB_TOKEN non configuré")
    return GitLabClient(settings.gitlab_url, settings.gitlab_token)


@router.get("/{project_id}")
async def get_branches(project_id: int):
    client = _client()
    branches = await client.get_branches(project_id)
    return [
        {
            "name": b["name"],
            "commit": b.get("commit", {}),
            "protected": b.get("protected", False),
        }
        for b in branches
    ]
