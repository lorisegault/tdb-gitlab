from datetime import datetime

from pydantic import BaseModel


class RepositoryBase(BaseModel):
    name: str
    description: str = ""
    default_branch: str = "main"


class RepositoryCreate(RepositoryBase):
    gitlab_id: int


class RepositoryResponse(RepositoryBase):
    id: int
    gitlab_id: int
    last_activity_at: datetime | None = None

    model_config = {"from_attributes": True}
