import asyncio
import signal
import logging

log = logging.getLogger("hydra.shutdown")


def zainstaluj(aplikacja):
    petla = asyncio.get_event_loop()

    def lagodne():
        log.info("Otrzymano sygnał zakończenia")
        for zadanie in asyncio.all_tasks(petla):
            zadanie.cancel()

    for sig in (signal.SIGINT, signal.SIGTERM):
        petla.add_signal_handler(sig, lagodne)
