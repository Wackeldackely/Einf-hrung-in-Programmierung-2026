# Aufgabe 06-01
#  TODO: Ihre Lösung hier

artikel = {
    "artikel_nr": "A-123",
    "name": "USB-C Hub",
    "preis": 49.99,
    "lagerbestand": "75",
}

print(f"Ursprünglicher Preis: {artikel['preis']} Euro")

neu_p = round(artikel["preis"] * 1.1, 2)

# artikel["preis"] = round(49.99 * 1.1, 2)
# round(preis * 1.19, 2)
# neu_p = artikel.get("neu_p")
# neuneu = neu_p *1.1

artikel["preis"] = neu_p
artikel["hersteller"] = "TechPrime"

print(f"Das aktualisierte Artikelprofil: {artikel}")
