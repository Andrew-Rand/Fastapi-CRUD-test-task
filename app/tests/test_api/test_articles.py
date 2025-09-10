import typing

import pytest
import pytest_asyncio
from httpx import AsyncClient

from app.core.articles.models import Article


@pytest_asyncio.fixture
async def article(async_client: AsyncClient) -> dict[str, typing.Any]:
    create = await async_client.post(
        "/articles",
        json={"title": "Test title", "content": "Test Content"},
        headers={"X-Client-ID": "client_a"},
    )
    assert create.status_code == 201
    return create.json()


class TestCreateArticle:
    @pytest.mark.asyncio
    async def test_create_item_if_ok(self, async_client: AsyncClient) -> None:
        resp = await async_client.post(
            "/articles",
            json={"title": "Test title", "content": "Test Content"},
            headers={"X-Client-ID": "client_a"},
        )
        assert resp.status_code == 201

        data = resp.json()

        assert data["title"] == "Test title"
        assert data["content"] == "Test Content"
        assert not data["author_id"]

    @pytest.mark.asyncio
    async def test_create_item_if_validation_error(self, async_client: AsyncClient) -> None:
        resp = await async_client.post(
            "/articles",
            json={"title": 123, "content": None},
            headers={"X-Client-ID": "client_a"},
        )
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_create_item_for_client_b(self, async_client: AsyncClient) -> None:
        resp = await async_client.post(
            "/articles",
            json={"title": "Test title", "content": "Test Content"},
            headers={"X-Client-ID": "client_b"},
        )
        assert resp.status_code == 403
        assert resp.json()["detail"] == "Endpoint not allowed for this client"


class TestGetArticle:
    @pytest.mark.asyncio
    async def test_get_item_if_ok(self, async_client: AsyncClient, article: dict[str, typing.Any]) -> None:
        resp = await async_client.get(
            f"/articles/{article['id']}",
            headers={"X-Client-ID": "client_a"},
        )
        assert resp.status_code == 200

        data = resp.json()

        assert data["id"] == article["id"]
        assert data["title"] == article["title"]
        assert data["content"] == article["content"]
        assert data["author_id"] == article["author_id"]

    @pytest.mark.asyncio
    async def test_get_item_if_not_found(self, async_client: AsyncClient) -> None:
        resp = await async_client.get(
            "/articles/0",
            headers={"X-Client-ID": "client_a"},
        )
        assert resp.status_code == 404

    @pytest.mark.asyncio
    async def test_get_item_if_client_b(self, async_client: AsyncClient, article: dict[str, typing.Any]) -> None:
        resp = await async_client.get(
            f"/articles/{article['id']}",
            headers={"X-Client-ID": "client_b"},
        )
        assert resp.status_code == 200

        data = resp.json()

        assert data["id"] == article["id"]
        assert data["title"] == article["title"]
        assert data["content"] == article["content"]
        assert "author_id" not in data


class TestArtileList:
    @pytest.mark.asyncio
    async def test_list_item_if_ok(self, async_client: AsyncClient, article: dict[str, typing.Any]) -> None:
        resp = await async_client.get(
            f"/articles",
            headers={"X-Client-ID": "client_a"},
        )
        data = resp.json()
        assert isinstance(data, list)

        for item in data:
            assert item["title"] == article["title"]
            assert item["content"] == article["content"]
            assert item["author_id"] == article["author_id"]

    @pytest.mark.asyncio
    async def test_list_item_if_pagination(self, async_client: AsyncClient, article: dict[str, typing.Any]) -> None:
        resp = await async_client.get(
            f"/articles",
            headers={"X-Client-ID": "client_a"},
            params={"limit": 1},
        )
        data = resp.json()
        assert isinstance(data, list)
        assert len(data) == 1

        for item in data:
            assert item["title"] == article["title"]
            assert item["content"] == article["content"]
            assert item["author_id"] == article["author_id"]

    @pytest.mark.asyncio
    async def test_list_item_if_client_b(self, async_client: AsyncClient, article: dict[str, typing.Any]) -> None:
        resp = await async_client.get(
            f"/articles",
            headers={"X-Client-ID": "client_b"},
        )
        data = resp.json()
        assert isinstance(data, list)

        for item in data:
            assert item["title"] == article["title"]
            assert item["content"] == article["content"]
            assert not "author_id" in item


class TestUpdateArticle:
    @pytest.mark.asyncio
    async def test_update_item_if_ok(self, async_client: AsyncClient, article: dict[str, typing.Any]) -> None:
        resp = await async_client.patch(
            f"/articles/{article['id']}",
            json={"title": "New title", "content": "New Content"},
            headers={"X-Client-ID": "client_a"},
        )
        assert resp.status_code == 200

        data = resp.json()

        assert data["title"] == "New title"
        assert data["content"] == "New Content"
        assert not data["author_id"]

    @pytest.mark.asyncio
    async def test_update_item_if_validation_error(self, async_client: AsyncClient, article: dict[str, typing.Any]) -> None:
        resp = await async_client.patch(
            f"/articles/{article['id']}",
            json={"title": 123, "content": 123},
            headers={"X-Client-ID": "client_a"},
        )
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_update_item_if_not_found(self, async_client: AsyncClient) -> None:
        resp = await async_client.patch(
            "/articles/0",
            json={"title": "New title", "content": "New Content"},
            headers={"X-Client-ID": "client_a"},
        )
        assert resp.status_code == 404

    @pytest.mark.asyncio
    async def test_update_item_for_client_b(self, async_client: AsyncClient) -> None:
        resp = await async_client.patch(
            f"/articles/1",
            json={"title": "Test title", "content": "Test Content"},
            headers={"X-Client-ID": "client_b"},
        )
        assert resp.status_code == 403
        assert resp.json()["detail"] == "Endpoint not allowed for this client"


class TestDeleteArticle:
    @pytest.mark.asyncio
    async def test_delete_item_if_ok(self, async_client: AsyncClient, article: dict[str, typing.Any]) -> None:
        resp = await async_client.delete(
            f"/articles/{article['id']}",
            headers={"X-Client-ID": "client_a"},
        )
        assert resp.status_code == 200
        assert resp.json()["detail"] == "Deleted"

    @pytest.mark.asyncio
    async def test_delete_item_if_not_found(self, async_client: AsyncClient) -> None:
        resp = await async_client.delete(
            "/articles/0",
            headers={"X-Client-ID": "client_a"},
        )
        assert resp.status_code == 404

    @pytest.mark.asyncio
    async def test_delete_item_if_client_b(self, async_client: AsyncClient) -> None:
        resp = await async_client.delete(
            "/articles/1",
            headers={"X-Client-ID": "client_b"},
        )
        assert resp.status_code == 403
        assert resp.json()["detail"] == "Endpoint not allowed for this client"