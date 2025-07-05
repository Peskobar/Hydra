class PamiecCache:
    def __init__(self) -> None:
        self._dane: dict[str, str] = {}

    def pobierz(self, klucz: str) -> str | None:
        return self._dane.get(klucz)

    def ustaw(self, klucz: str, wartosc: str) -> None:
        self._dane[klucz] = wartosc

    def usun(self, klucz: str) -> None:
        self._dane.pop(klucz, None)
