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


class MergeRequestBase(BaseModel):
    gitlab_id: int
    project_id: int
    title: str
    author: str
    state: str = "opened"
    comments_count: int = 0
    approvals_count: int = 0


class MergeRequestCreate(MergeRequestBase):
    pass


class MergeRequestResponse(MergeRequestBase):
    id: int
    created_at: datetime | None = None

    model_config = {"from_attributes": True}


class IssueBase(BaseModel):
    gitlab_id: int
    project_id: int
    title: str
    author: str
    priority: str = "medium"
    labels: str = ""
    assignee: str | None = None
    due_date: datetime | None = None
    state: str = "opened"


class IssueCreate(IssueBase):
    pass


class IssueResponse(IssueBase):
    id: int
    created_at: datetime | None = None

    model_config = {"from_attributes": True}


class PipelineBase(BaseModel):
    gitlab_id: int
    project_id: int
    status: str
    duration: int | None = None
    branch: str = "main"


class PipelineCreate(PipelineBase):
    pass


class PipelineResponse(PipelineBase):
    id: int
    created_at: datetime | None = None

    model_config = {"from_attributes": True}
