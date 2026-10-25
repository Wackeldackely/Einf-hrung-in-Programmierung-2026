# Aufgabe 04-04
#  TODO: Ihre Lösung hier

liste = [10, -5, 20, 0, -15, 8]
summe = 0

for i in liste:
    if i < 0:
        print(f"Ignoriere negative Zahl: {i}")
        continue

    elif i > 0:
        summe += i
        print(f"Die Summe der positiven Zahlen ist: {summe}")
