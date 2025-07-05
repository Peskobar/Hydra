import typer
from sqlalchemy.orm import Session
from .database.session import SesjaSync
from .database.models import Uzytkownik, StatusKonta

cli = typer.Typer(help="Hydra – narzędzia administracyjne")


@cli.command()
def lista(status: StatusKonta | None = typer.Option(None, help="Filtr statusu")) -> None:
    db: Session = SesjaSync()
    q = db.query(Uzytkownik)
    if status:
        q = q.filter(Uzytkownik.status == status)
    for u in q.limit(100):
        typer.echo(f"{u.id}\t{u.email}\t{u.status}")


@cli.command()
def ban(uid: int) -> None:
    db: Session = SesjaSync()
    u = db.query(Uzytkownik).get(uid)
    if u:
        u.status = StatusKonta.BANNED
        db.commit()
        typer.echo("Oznaczono jako BANNED")


if __name__ == "__main__":
    cli()
