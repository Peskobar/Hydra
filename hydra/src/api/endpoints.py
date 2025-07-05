from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database.session import SesjaAsync
from ..database import models


async def pobierz_sesje() -> AsyncSession:
    async with SesjaAsync() as sesja:
        yield sesja


def dodaj_http(app: FastAPI) -> None:
    @app.get("/uzytkownicy")
    async def lista(sesja: AsyncSession = Depends(pobierz_sesje)):
        wynik = await sesja.execute(models.Uzytkownik.__table__.select())
        return wynik.mappings().all()
