from src.core.banrate import LicznikBlokad


def test_banrate():
    licznik = LicznikBlokad()
    licznik.dodaj_probe(True)
    licznik.dodaj_probe(False)
    assert licznik.wspolczynnik == 0.5
