# Projekt Hydra

Hydra to asynchroniczny serwis oparty o FastAPI z modułem P2P i zestawem
workerów. System został zaprojektowany do łatwego rozszerzania i monitorowania.

```
          +------------+
          |  Klient    |
          +------+-----+
                 |
                 v
 +---------------+---------------+
 |  FastAPI (api/main.py)        |
 +---------------+---------------+
                 |
                 v
        +--------+---------+
        |  Baza danych      |
        +-------------------+
                 |
                 v
        +--------+---------+
        |  Workerzy         |
        +-------------------+
```

## Szybki start

1. Zainstaluj zależności: `pip install -r requirements.txt`.
2. Uruchom aplikację: `uvicorn src.api.main:stworz_aplikacje`.
3. Włącz workerów za pomocą `python -m src.workers.proxy_harvester` itd.

## Roadmap

- [ ] Rozszerzenie komunikacji P2P o szyfrowanie.
- [ ] Integracja z zewnętrznym systemem kolejkowania zadań.
- [ ] Lepsze testy end-to-end w Playwright.

