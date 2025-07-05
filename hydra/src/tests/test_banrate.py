from src.core.banrate import LicznikBlokad


def test_banrate():
    l = LicznikBlokad()
    l.dodaj_probe(True)
    l.dodaj_probe(False)
    assert l.wspolczynnik == 0.5
