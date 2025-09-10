import pytest

from app.common.tools import check_id_domain


@pytest.mark.asyncio
@pytest.mark.parametrize('source,expected', [('/articles', '/articles'), ('/articles/1', '/articles/{id}')])
async def test_check_id_domain(source: str, expected: str) -> None:
    assert check_id_domain(source) == expected