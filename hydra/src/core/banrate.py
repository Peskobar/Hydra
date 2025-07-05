class LicznikBlokad:
    def __init__(self) -> None:
        self._proby = 0
        self._blokady = 0

    def dodaj_probe(self, udana: bool) -> None:
        self._proby += 1
        if not udana:
            self._blokady += 1

    @property
    def wspolczynnik(self) -> float:
        if self._proby == 0:
            return 0.0
        return self._blokady / self._proby
