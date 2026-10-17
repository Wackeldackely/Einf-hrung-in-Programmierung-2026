# Aufgabe 03-04
#  TODO: Ihre Lösung hier

zahl1 = float(input("Gib die erste Zahl ein:"))
zahl2 = float(input("Gib die zweite Zahl ein:"))
operation = input("Gib die Operation ein (+, -, *, /):")


if operation == "+":
    ergebnis = float(zahl1 + zahl2)

elif operation == "-":
    ergebnis = float(zahl1 - zahl2)

elif operation == "*":
    ergebnis = float(zahl1 * zahl2)

elif operation == "/":
    if zahl2 == 0:
        print("Fehler: Division durch 0 ist nicht definiert!")
    else:
        ergebnis = float(zahl1 / zahl2)


print(f"Das Ergebnis von {zahl1} {operation} {zahl2} ist: {ergebnis:.2f}")


# elif operation == "/":
# ergebnis = float(zahl1 / zahl2)

# if zahl2 == "0":
# print("Fehler: Division durch 0 ist nicht definiert!")
