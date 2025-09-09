import pytest

@pytest.mark.asyncio
async def test_create_item(async_client):
    create = await async_client.post("/articles", json={"title": "Test title", "content": "Test Content"}, headers={"X-Client-ID": "client_a"})
    item_id = create.json()["id"]

    delete = await async_client.delete(f"/items/{item_id}")
    assert delete.status_code == 200
    assert delete.json()["ok"] is True