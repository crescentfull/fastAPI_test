import pytest
from httpx import AsyncClient
from main import app

async def test_create_article_returns_201():
    async with AsyncClient(app=app, base_url="http://test") as client:
