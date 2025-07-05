from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String

Baza = declarative_base()


class Uzytkownik(Baza):
    __tablename__ = "uzytkownicy"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
