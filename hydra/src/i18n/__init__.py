from babel.support import Translations
import pathlib

_LOCALE_DIR = pathlib.Path("locales")
_trans = Translations.load(dirname=_LOCALE_DIR, locales=["pl"])

def _(msg: str) -> str:
    return _trans.gettext(msg)
