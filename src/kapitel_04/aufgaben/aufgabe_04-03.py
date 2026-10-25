# Aufgabe 04-03
#  TODO: Ihre Lösung hier

# artikel = [",
# ]

# print("Gib einen Artikel für die Einkaufsliste ein (oder 'fertig' zum Beenden):")
# print("--- Deine Einkaufsliste ---")


einkauf = []
print("Gib einen Artikel für die Einkaufsliste ein (oder 'fertig' zum Beenden):")


while True:
    artikel = input("Gib einen Artikel für die Einkaufsliste ein:")
    # einkauf = [artikel]
    if artikel == "fertig":
        break
    else:
        einkauf.append(artikel)

print("--- Deine Einkaufsliste ---")
for artikel in einkauf:
    print(artikel)
