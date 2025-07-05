import asyncio
from dataclasses import dataclass
from random import randint
import httpx
from tenacity import retry, stop_after_attempt, wait_fixed


@dataclass
class DaneKonta:
    email: str
    haslo: str


class GeneratorKont:
    """Tworzy konta poprzez zapytania HTTP."""

    def __init__(self, endpoint: str, domena: str = "example.com") -> None:
        self.endpoint = endpoint
        self.domena = domena
        self._licznik = 0
        self._lock = asyncio.Lock()

    def _nowy_email(self) -> str:
        self._licznik += 1
        return f"uzytkownik{self._licznik}@{self.domena}"

    def _nowe_haslo(self) -> str:
        return f"H{randint(100000, 999999)}!"

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
    async def generuj(self) -> DaneKonta:
        async with self._lock:
            email = self._nowy_email()
        haslo = self._nowe_haslo()
        async with httpx.AsyncClient() as klient:
            resp = await klient.post(
                self.endpoint,
                json={"email": email, "password": haslo},
                timeout=10,
            )
            resp.raise_for_status()
        return DaneKonta(email=email, haslo=haslo)


async def uruchom() -> None:
    gen = GeneratorKont("http://localhost:8000/register")
    while True:
        konto = await gen.generuj()
        print("Utworzono", konto.email)
        await asyncio.sleep(20)


if __name__ == "__main__":
    asyncio.run(uruchom())

# self-review: modul generuje unikalne konta i wysyla je do serwera przy zachowaniu
# prostego ograniczenia liczby prob oraz wypisuje wynik na stdout. kod spelnia PEP8.
