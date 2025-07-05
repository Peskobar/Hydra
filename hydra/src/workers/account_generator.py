import asyncio
from tenacity import retry, stop_after_attempt


class GeneratorKont:
    def __init__(self) -> None:
        self.licznik = 0

    @retry(stop=stop_after_attempt(3))
    async def generuj(self) -> dict[str, str]:
        await asyncio.sleep(0.1)
        self.licznik += 1
        return {"email": f"user{self.licznik}@example.com"}


async def uruchom():
    gen = GeneratorKont()
    while True:
        await gen.generuj()
        await asyncio.sleep(20)


if __name__ == "__main__":
    asyncio.run(uruchom())
