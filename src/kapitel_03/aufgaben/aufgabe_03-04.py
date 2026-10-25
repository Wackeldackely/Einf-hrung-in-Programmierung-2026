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

# man müsste bei jedem elif unter die Bestimmung des ergebnisses noch den print Befehl hinzufügen, damit bei einer Fehlermeldung von /0 nicht noch das ergebins neu aufgeschrieben wird, sondern nur die Fehlermeldung angezeigt wird

# elif operation == "/":
# ergebnis = float(zahl1 / zahl2)

# if zahl2 == "0":
# print("Fehler: Division durch 0 ist nicht definiert!")
