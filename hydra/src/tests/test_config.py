from src.core.config import Konfiguracja


def test_domyslne():
    cfg = Konfiguracja()
    assert "sqlite" in cfg.baza_danych
