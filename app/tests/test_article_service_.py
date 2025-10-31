import pytest
from httpx import AsyncClient
from main import app
from app.db.session import engine
from sqlmodel import SQLModel

def setup_db():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


