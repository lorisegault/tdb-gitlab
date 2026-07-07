import tempfile

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

_db_file = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
_test_db_url = f"sqlite:///{_db_file.name}"

settings.database_url = _test_db_url

import app.database as db_mod

_test_engine = create_engine(_test_db_url, connect_args={"check_same_thread": False})
_test_session_local = sessionmaker(bind=_test_engine, autoflush=False)

db_mod.get_engine = lambda: _test_engine
db_mod.get_session_local = lambda: _test_session_local

from app.database import Base
from app.main import app


@pytest.fixture(autouse=True)
def _setup_db():
    Base.metadata.create_all(bind=_test_engine)
    yield
    Base.metadata.drop_all(bind=_test_engine)


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
