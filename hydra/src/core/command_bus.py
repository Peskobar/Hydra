from collections.abc import Callable
from typing import Any, Dict


class MagistralaPolecen:
    def __init__(self) -> None:
        self._subskrypcje: Dict[str, list[Callable[[Any], None]]] = {}

    def subskrybuj(self, nazwa: str, handler: Callable[[Any], None]) -> None:
        self._subskrypcje.setdefault(nazwa, []).append(handler)

    def wyslij(self, nazwa: str, dane: Any) -> None:
        for handler in self._subskrypcje.get(nazwa, []):
            handler(dane)
