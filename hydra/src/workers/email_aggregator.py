import asyncio
from tenacity import retry, stop_after_attempt


class AgregatorEmaili:
    def __init__(self) -> None:
        self.kolejka: list[str] = []

    @retry(stop=stop_after_attempt(3))
    async def wyslij(self, email: str) -> None:
        await asyncio.sleep(0.1)
        self.kolejka.append(email)


async def uruchom():
    ag = AgregatorEmaili()
    while True:
        await ag.wyslij("test@example.com")
        await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(uruchom())
