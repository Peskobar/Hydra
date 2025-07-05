import asyncio
import httpx
from tenacity import retry, stop_after_attempt


class ZbieraczProxy:
    def __init__(self, url: str) -> None:
        self.url = url
        self.proxies: list[str] = []

    @retry(stop=stop_after_attempt(3))
    async def pobierz(self) -> None:
        async with httpx.AsyncClient() as klient:
            odp = await klient.get(self.url)
            odp.raise_for_status()
            self.proxies = odp.text.splitlines()


async def uruchom():
    zbieracz = ZbieraczProxy("https://example.com/proxy.txt")
    while True:
        try:
            await zbieracz.pobierz()
        except Exception:
            pass
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(uruchom())
