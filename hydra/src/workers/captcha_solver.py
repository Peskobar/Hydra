import asyncio
from tenacity import retry, stop_after_attempt


class RozwiazywaczCaptcha:
    def __init__(self) -> None:
        self.ilosc = 0

    @retry(stop=stop_after_attempt(5))
    async def rozwiaz(self, obrazek: bytes) -> str:
        await asyncio.sleep(0.1)
        self.ilosc += 1
        return "odpowiedz"


async def uruchom():
    solver = RozwiazywaczCaptcha()
    while True:
        await solver.rozwiaz(b"dane")
        await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(uruchom())
