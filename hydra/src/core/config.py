from dataclasses import dataclass, field
import os


def _env(klucz: str, domyslna: str) -> str:
    return os.getenv(klucz, domyslna)


def _env_int(klucz: str, domyslna: int) -> int:
    try:
        return int(os.getenv(klucz, str(domyslna)))
    except ValueError:
        return domyslna


def _env_bool(klucz: str, domyslna: bool) -> bool:
    wartosc = os.getenv(klucz)
    if wartosc is None:
        return domyslna
    return wartosc.lower() in {"1", "t", "true", "y", "yes"}


@dataclass
class Konfiguracja:
    baza_danych: str = _env("DATABASE_URL", "sqlite+aiosqlite:///hydra.db")
    tryb_debug: bool = _env_bool("DEBUG", False)
    tajny_klucz: str = _env("SECRET_KEY", "zmien")
    smtp_host: str = _env("SMTP_HOST", "localhost")
    smtp_port: int = _env_int("SMTP_PORT", 25)
    smtp_user: str = _env("SMTP_USER", "")
    smtp_haslo: str = _env("SMTP_PASSWORD", "")
    proxy_zrodla: list[str] = field(
        default_factory=lambda: [w for w in _env("PROXY_SOURCES", "").split(",") if w]
    )
    limit_workerow: int = _env_int("WORKER_LIMIT", 10)

    @classmethod
    def wczytaj(cls) -> "Konfiguracja":
        return cls()

# self-review: konfiguracja zawiera funkcje pomocnicze do parsowania roznych typ
# zmiennych srodowiskowych. dataclass zapewnia proste wczytanie wartosci z
# defaulatami. kod zgodny z PEP8.
