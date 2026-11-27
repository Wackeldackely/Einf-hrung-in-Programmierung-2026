# Aufgabe 09-02
#  TODO: Ihre Lösung hier

import json
import os

config_ini = {}
# config_ini["username"] = "admin"

with open("config.ini", "w", encoding="utf-8") as f:
    f.write("username=admin\n")
    f.write("theme=dark\n")
    f.write("language=de\n")

    # json.dump(config_ini, f)
    # with open("config.ini", "r", encoding="utf-8") as f:
    # for zeile in f:
    #  ausgegebene_liste = zeile.strip().split("=")
    # config_ini[ausgegebene_liste[0]] = ausgegebene_liste[1]


try:
    print(f"Versuche Datei 'config.ini' zu öffen...")
    with (
        open("config.ini", "r", encoding="utf-8") as f
    ):  # fehlermeldung wird ausgelöst, wenn anstatt "config.ini" nun etwas anderes stehen würde, da der dateiname nicht mehr übereinstimmen würde
        for zeile in f:
            ausgegebene_liste = zeile.strip().split("=")
            config_ini[ausgegebene_liste[0]] = ausgegebene_liste[1]
        print(config_ini)

except FileNotFoundError as e:
    print(
        f"Fehler: Konfigurationdatei'config.ini' nicht gefunden. Standartwerte werden verwendet.\nKonfiguration geladen:"
    )
