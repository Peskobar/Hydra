from datetime import datetime


class Historia:
    def __init__(self) -> None:
        self._wydarzenia: list[tuple[datetime, str]] = []

    def dodaj(self, wiadomosc: str) -> None:
        self._wydarzenia.append((datetime.utcnow(), wiadomosc))

    def ostatnie(self, limit: int = 20) -> list[str]:
        return [w for _, w in self._wydarzenia[-limit:]]
