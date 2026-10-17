# Aufgabe 03-01
#  TODO: Ihre Lösung hier

Punktzahl = int(input("Bitte gib deine erreichte Punktzahl ein:"))

if Punktzahl >= 90:
    print(f"Deine Note: Sehr gut {Punktzahl} ")

elif Punktzahl >= 80:
    print(f"Deine Note: Gut {Punktzahl}")

elif Punktzahl >= 65:
    print(f"Deine Note: Befriedigend {Punktzahl}")

elif Punktzahl >= 50:
    print(f"Deine Note: Ausreichend {Punktzahl}")

# else:
# print(f"Deine Note: Nicht bestanden {Punktzahl}")

# oder in der letzten zeile anstatt else:
elif Punktzahl >= 0:
    print(f"Deine Note: Nicht bestanden {Punktzahl}")
