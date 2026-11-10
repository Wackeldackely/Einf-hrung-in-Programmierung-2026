# Aufgabe 05-01
#  TODO: Ihre Lösung hier

noten = [88, 92, 77, 95, 81]

print(f"Ursprüngliche Noten: {noten}")

noten.sort()

print(f"Schlechtes Ergebnis {noten[0]} entfernt. ")

del noten[0]

noten.append(94)

print("Note 94 hinzugefügt.")

noten.sort()

print(f"Finale Notenliste: {noten}")

durchschnitt = float(sum(noten) // len(noten))

print(f"Neuer Durchschnitt: {durchschnitt}")
