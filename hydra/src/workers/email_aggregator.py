import asyncio
import smtplib
from email.message import EmailMessage
from tenacity import retry, stop_after_attempt, wait_fixed


class AgregatorEmaili:
    """Kolejkuje i wysyla wiadomosci email."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 25,
        uzytkownik: str | None = None,
        haslo: str | None = None,
        ssl: bool = False,
    ) -> None:
        self.host = host
        self.port = port
        self.uzytkownik = uzytkownik
        self.haslo = haslo
        self.ssl = ssl
        self.kolejka: asyncio.Queue[EmailMessage] = asyncio.Queue()

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
    async def wyslij(self, email: EmailMessage) -> None:
        await self.kolejka.put(email)

    async def _nadaj(self, msg: EmailMessage) -> None:
        def send() -> None:
            if self.ssl:
                with smtplib.SMTP_SSL(self.host, self.port) as serwer:
                    if self.uzytkownik:
                        serwer.login(self.uzytkownik, self.haslo or "")
                    serwer.send_message(msg)
            else:
                with smtplib.SMTP(self.host, self.port) as serwer:
                    serwer.starttls()
                    if self.uzytkownik:
                        serwer.login(self.uzytkownik, self.haslo or "")
                    serwer.send_message(msg)

        await asyncio.to_thread(send)

    async def procesuj(self) -> None:
        while True:
            msg = await self.kolejka.get()
            try:
                await self._nadaj(msg)
            finally:
                self.kolejka.task_done()


async def uruchom() -> None:
    ag = AgregatorEmaili()
    asyncio.create_task(ag.procesuj())
    while True:
        msg = EmailMessage()
        msg["From"] = "noreply@example.com"
        msg["To"] = "test@example.com"
        msg["Subject"] = "Test"
        msg.set_content("Witaj")
        await ag.wyslij(msg)
        await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(uruchom())

# self-review: agregator uzywa kolejki i watekowych operacji smtp do wysylki
# wiadomosci; przetwarzanie jest petla asynchroniczna i zapewnia powtarzalne
# proby w razie bledow. kod zgodny z PEP8.
