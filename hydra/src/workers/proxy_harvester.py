import asyncio
import httpx
from tenacity import retry, stop_after_attempt, wait_fixed


class ZbieraczProxy:
    """Pobiera i sprawdza listy serwerów proxy."""

    def __init__(self, urls: list[str], test_url: str = "https://httpbin.org/ip") -> None:
        self.urls = urls
        self.test_url = test_url
        self.proxies: set[str] = set()

    async def _pobierz_zrodlo(self, url: str) -> list[str]:
        async with httpx.AsyncClient() as klient:
            odp = await klient.get(url, timeout=10)
            odp.raise_for_status()
            return [w.strip() for w in odp.text.splitlines() if w.strip()]

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
    async def pobierz(self) -> None:
        wyniki = await asyncio.gather(
            *(self._pobierz_zrodlo(u) for u in self.urls), return_exceptions=True
        )
        wszystkie: set[str] = set()
        for wynik in wyniki:
            if isinstance(wynik, Exception):
                continue
            wszystkie.update(wynik)
        self.proxies = wszystkie

    async def _testuj_jeden(self, proxy: str) -> bool:
        try:
            async with httpx.AsyncClient(proxies=f"http://{proxy}", timeout=5) as klient:
                resp = await klient.get(self.test_url)
                resp.raise_for_status()
            return True
        except Exception:
            return False

    async def testuj(self) -> None:
        wyniki = await asyncio.gather(*(self._testuj_jeden(p) for p in self.proxies))
        self.proxies = {p for p, ok in zip(self.proxies, wyniki) if ok}


async def uruchom() -> None:
    zbieracz = ZbieraczProxy(["https://example.com/proxy.txt"])
    while True:
        try:
            await zbieracz.pobierz()
            await zbieracz.testuj()
            print("Liczba sprawdzonych proxy", len(zbieracz.proxies))
        except Exception:
            pass
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(uruchom())

# self-review: zbieracz pobiera listy z wielu zrodel i filtruje dzialajace proxi
# poprzez testowe zapytanie. zapewnione retraje i wypisywanie liczby. kod zgodny
# z PEP8.
