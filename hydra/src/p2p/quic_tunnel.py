import asyncio


class TunelQuic:
    def __init__(self, adres: str) -> None:
        self.adres = adres

    async def przeslij(self, dane: bytes) -> bytes:
        await asyncio.sleep(0.01)
        return dane[::-1]
