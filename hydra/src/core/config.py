from dataclasses import dataclass
import os


def env(klucz: str, domyslna: str) -> str:
    return os.getenv(klucz, domyslna)


@dataclass
class Konfiguracja:
    baza_danych: str = env("DATABASE_URL", "sqlite+aiosqlite:///hydra.db")
    tryb_debug: bool = env("DEBUG", "0") == "1"
    tajny_klucz: str = env("SECRET_KEY", "zmien")
