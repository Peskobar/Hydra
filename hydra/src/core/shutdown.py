import asyncio
import signal
import logging
from .http import _Client

_log = logging.getLogger("hydra.shutdown")


def zainstaluj(aplikacja):
    petla = asyncio.get_event_loop()

    def lagodne():
        _log.info("Otrzymano sygnał – zamykam łagodnie…")
        for zadanie in asyncio.all_tasks(petla):
            zadanie.cancel()

    for sig in (signal.SIGINT, signal.SIGTERM):
        petla.add_signal_handler(sig, lagodne)

    petla.create_task(_Client.close())
