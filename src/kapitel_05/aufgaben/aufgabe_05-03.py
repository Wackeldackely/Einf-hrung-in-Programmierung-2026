# Aufgabe 05-03
#  TODO: Ihre Lösung hier

lagerbestand = [("Laptop", 15), ("Maus", 35), ("Tastatur", 8), ("Bildschirm", 5)]

# anteil_laptop = lagerbestand[0]
# anteil_maus = lagerbestand[1]
# anteil_tastatur = lagerbestand[2]
# anteil_bildschirm = lagerbestand[3]
# anteile = [anteil_laptop, anteil_maus, anteil_tastatur, anteil_bildschirm]
# index_tastatur = lagerbestand.index(("Tastatur", 8))

print("Kritischer Lagerbestand (unter 10 Stück):")

for i in lagerbestand:
    if i[1] < 10:
        print(f"{i[1 - 1]}: {i[1]} Stück")
