import httpx
import asyncio


class _Client:
    _client: httpx.AsyncClient | None = None

    @classmethod
    def get(cls) -> httpx.AsyncClient:
        if cls._client is None:
            cls._client = httpx.AsyncClient(
                limits=httpx.Limits(max_keepalive_connections=50, max_connections=100),
                timeout=15.0,
                verify=False,
            )
        return cls._client

    @classmethod
    async def close(cls) -> None:
        if cls._client:
            await cls._client.aclose()
            cls._client = None
