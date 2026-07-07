from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from app.database import Base


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True)
    gitlab_id = Column(Integer, unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, default="")
    default_branch = Column(String(255), default="main")
    last_activity_at = Column(DateTime, nullable=True)


class MergeRequest(Base):
    __tablename__ = "merge_requests"

    id = Column(Integer, primary_key=True)
    gitlab_id = Column(Integer, nullable=False)
    project_id = Column(Integer, ForeignKey("repositories.gitlab_id"), nullable=False)
    title = Column(String(500), nullable=False)
    author = Column(String(255), nullable=False)
    state = Column(String(50), default="opened")
    comments_count = Column(Integer, default=0)
    approvals_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)


class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True)
    gitlab_id = Column(Integer, nullable=False)
    project_id = Column(Integer, ForeignKey("repositories.gitlab_id"), nullable=False)
    title = Column(String(500), nullable=False)
    author = Column(String(255), nullable=False)
    priority = Column(String(50), default="medium")
    labels = Column(String(500), default="")
    assignee = Column(String(255), nullable=True)
    due_date = Column(DateTime, nullable=True)
    state = Column(String(50), default="opened")
    created_at = Column(DateTime, default=datetime.utcnow)


class Pipeline(Base):
    __tablename__ = "pipelines"

    id = Column(Integer, primary_key=True)
    gitlab_id = Column(Integer, nullable=False)
    project_id = Column(Integer, ForeignKey("repositories.gitlab_id"), nullable=False)
    status = Column(String(50), nullable=False)
    duration = Column(Integer, nullable=True)
    branch = Column(String(255), default="main")
    created_at = Column(DateTime, default=datetime.utcnow)
