# Aufgabe 09-04
#  TODO: Ihre Lösung hier

import json

order = {
    "bestell_nr": "B-2025-42",
    "kunde": "Max Mustermann",
    "artikel": [
        {
            "produkt_id": "A-123",
            "name": "Gaming-Maus",
            "menge": 1,
            "preis_pro_stueck": 79.99,
        },
        {
            "produkt_id": "C-789",
            "name": "USB-C Kabel",
            "menge": 3,
            "preis_pro_stueck": 9.50,
        },
    ],
}

with open("order.json", "w", encoding="utf-8") as f:
    json.dump(order, f, indent=4)

with open("order.json", "r", encoding="utf-8") as f:
    order = json.load(f)
# benötigte Rechnung: von bestellnummer B-2025-42: die artikelmenge * den Artikelpreis der einzelnen Artikel und diese dann addieren

gesamt_preis = sum(
    [
        position.get("menge") * position.get("preis_pro_stueck")
        for position in order.get("artikel")
    ]
)  # man addiert mit sum die Rechnung von den Positionen, also den dictionaries in artikel
print(f"Gesamtpreis für Bestellung B-2025-42: {gesamt_preis} Euro")
