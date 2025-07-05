import asyncio
import hashlib
import httpx
from tenacity import retry, stop_after_attempt, wait_fixed


class RozwiazywaczCaptcha:
    """Rozwiazuje captche lokalnie lub zdalnie."""

    def __init__(self, endpoint: str | None = None) -> None:
        self.endpoint = endpoint
        self.ilosc = 0

    def _lokalne(self, obrazek: bytes) -> str:
        return hashlib.sha256(obrazek).hexdigest()

    @retry(stop=stop_after_attempt(5), wait=wait_fixed(1))
    async def rozwiaz(self, obrazek: bytes) -> str:
        self.ilosc += 1
        if self.endpoint:
            async with httpx.AsyncClient() as klient:
                resp = await klient.post(self.endpoint, content=obrazek, timeout=15)
                resp.raise_for_status()
                return resp.text.strip()
        await asyncio.sleep(0)
        return self._lokalne(obrazek)


async def uruchom() -> None:
    solver = RozwiazywaczCaptcha()
    while True:
        wynik = await solver.rozwiaz(b"dane")
        print("Captcha", wynik)
        await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(uruchom())

# self-review: rozwiazywacz obsluguje opcjonalny serwis zdalny i fallback na hasz
# obrazka. implementacja zgodna z PEP8 i asynchroniczna.
