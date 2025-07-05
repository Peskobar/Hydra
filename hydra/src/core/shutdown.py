import asyncio
import signal
import logging
from .http import _Client

log = logging.getLogger("hydra.shutdown")


def zainstaluj(aplikacja):
    petla = asyncio.get_event_loop()

    def lagodne():
        log.info("Otrzymano sygnał zakończenia")
        for zadanie in asyncio.all_tasks(petla):
            zadanie.cancel()
        petla.create_task(_Client.close())

    for sig in (signal.SIGINT, signal.SIGTERM):
        petla.add_signal_handler(sig, lagodne)
