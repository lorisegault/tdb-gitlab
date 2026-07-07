from sqlalchemy import Column, Integer, String, DateTime, Text

from app.database import Base


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True)
    gitlab_id = Column(Integer, unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, default="")
    default_branch = Column(String(255), default="main")
    last_activity_at = Column(DateTime, nullable=True)
