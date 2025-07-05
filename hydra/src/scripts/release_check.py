import json
import sys


def sprawdz(manifest: str) -> None:
    with open(manifest) as f:
        dane = json.load(f)
    for plik in dane:
        if plik.get("bytes", 0) <= 0:
            print("Nieprawidłowy wpis w manifeście")
            sys.exit(1)


if __name__ == "__main__":
    sciezka = sys.argv[1] if len(sys.argv) > 1 else "MANIFEST.json"
    sprawdz(sciezka)
