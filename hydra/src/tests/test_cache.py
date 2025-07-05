from src.core.cache import PamiecCache


def test_cache():
    c = PamiecCache()
    c.ustaw("a", "1")
    assert c.pobierz("a") == "1"
    c.usun("a")
    assert c.pobierz("a") is None
