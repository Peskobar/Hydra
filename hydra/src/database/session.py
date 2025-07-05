from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from ..core.config import Konfiguracja
from .models import Baza

config = Konfiguracja()

silnik = create_async_engine(config.baza_danych, echo=config.tryb_debug)
SesjaAsync = async_sessionmaker(silnik, expire_on_commit=False)


async def inicjuj() -> None:
    async with silnik.begin() as polaczenie:
        await polaczenie.run_sync(Baza.metadata.create_all)
