import pytest
from httpx import AsyncClient, ASGITransport
from importlib import import_module


@pytest.mark.asyncio
async def test_uzytkownicy(monkeypatch):
    monkeypatch.setattr("src.core.tracing.inicjuj_sledzenie", lambda app: None)
    mod = import_module("src.api.main")
    app = mod.stworz_aplikacje()

    async def faux_exec(q):
        class Res:
            class M:
                def all(self_inner):
                    return [{"id": 1, "email": "x"}]

            def mappings(self):
                return self.M()
        return Res()

    async def faux_get():
        return

    monkeypatch.setattr("src.database.session.SesjaAsync", lambda: None)
    monkeypatch.setattr("src.database.models.Uzytkownik.__table__.select", lambda: None)
    monkeypatch.setattr("sqlalchemy.ext.asyncio.AsyncSession.execute", lambda self, q: faux_exec(q))

    transport = ASGITransport(app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.get("/uzytkownicy")
        assert resp.status_code == 200
