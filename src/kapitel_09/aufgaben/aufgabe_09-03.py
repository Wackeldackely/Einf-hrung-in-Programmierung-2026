# Aufgabe 09-03
#  TODO: Ihre Lösung hier

import csv

# kundendaten = {"kunden_nr": {"K001", "K002", "K003"}, "name" : {"Anna Schmidt", "Ben Meier", "Clara Wolf"}, "stadt": {"Berlin", "München", "Hamburg"}}

kundendaten = [
    {"kunden_nr": "K001", "name": "Anna Schmidt", "stadt": "Berlin"},
    {"kunden_nr": "K002", "name": "Ben Meier", "stadt": "München"},
    {"kunden_nr": "K003", "name": "Clara Wolf", "stadt": "Hamburg"},
]

spalten_namen = ["kunden_nr", "name", "stadt"]

with open("kundendaten.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=spalten_namen)
    writer.writeheader()
    writer.writerows(kundendaten)

with open("kundendaten.csv", "r", newline="", encoding="utf-8") as csvfile:
    print(csvfile.read())
