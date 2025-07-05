from fastapi import FastAPI
from ..core.tracing import inicjuj_sledzenie
from ..core.shutdown import zainstaluj
from . import endpoints, endpoints_ws


def stworz_aplikacje() -> FastAPI:
    app = FastAPI()
    inicjuj_sledzenie(app)
    zainstaluj(app)
    endpoints.dodaj_http(app)
    endpoints_ws.dodaj_ws(app)
    return app

aplikacja = stworz_aplikacje()
