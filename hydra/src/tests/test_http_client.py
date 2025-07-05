import pytest
from src.core.http import _Client


@pytest.mark.asyncio
async def test_singleton_http_client():
    c1 = _Client.get()
    c2 = _Client.get()
    assert c1 is c2
    await _Client.close()
