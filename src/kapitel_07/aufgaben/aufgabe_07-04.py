# Aufgabe 07-04
#  TODO: Ihre Lösung hier

produkte = [
    {"name": "Laptop", "preis_netto": 1199.00},
    {"name": "Maus", "preis_netto": 25.00},
    {"name": "Tastatur", "preis_netto": 79.50},
]

# brutto = [preis["preis_netto"] for preis in produkte]

brutto_brerechnung = list(
    map(
        lambda preis: preis | {"preis_brutto": round(preis["preis_netto"] * 1.19, 2)},
        produkte,
    )
)

# produkte["preis_brutto"] = brutto_brerechnung
print(brutto_brerechnung)
