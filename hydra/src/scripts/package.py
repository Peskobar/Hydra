import json
import os
import zipfile
import hashlib
import sys


def zpakuj() -> None:
    manifest_path = os.getenv("MANIFEST", "MANIFEST.json")
    with open(manifest_path) as f:
        manifest = {e["path"]: e["bytes"] for e in json.load(f)}

    suma_manifest = sum(manifest.values())
    suma_rzeczywista = 0
    with zipfile.ZipFile("hydra.zip", "w") as z:
        for sciezka in manifest:
            z.write(sciezka)
            suma_rzeczywista += os.path.getsize(sciezka)

    if abs(suma_rzeczywista - suma_manifest) / suma_manifest > 0.05:
        print("Rozmiar niezgodny z manifestem")
        sys.exit(1)

    with open("hydra.zip", "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    print("SHA256:", sha)


if __name__ == "__main__":
    zpakuj()
