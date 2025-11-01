import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

pytestmark = pytest.mark.anyio("asyncio")

# 1단계: 작성글 생성 + 응답 JSON 검증 테스트
async def test_create_article_returns_json_fields():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        article_data = {
            "title": "두 번째 글",
            "description": "테스트 설명",
            "body": "본문 내용"
        }
        response = await client.post("/articles", json=article_data)

    # --- RED 조건 ---
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == article_data["title"]
    assert data["body"] == article_data["body"]
