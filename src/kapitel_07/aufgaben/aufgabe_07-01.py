# Aufgabe 07-01
#  TODO: Ihre Lösung hier


def berechne(zahl1: float, zahl2: float, operator: str) -> float | str:
    if operator == "+":
        ergebnis = float(zahl1 + zahl2)

    elif operator == "-":
        ergebnis = float(zahl1 - zahl2)

    elif operator == "*":
        ergebnis = float(zahl1 * zahl2)

    elif operator == "/":
        if zahl2 == 0:
            return "Fehler: Division durch 0 ist nicht definiert!"  # ganz wichtig, da das programm sonst abstürzt, da es versuchen würde ergebnis auszugeben!!
    else:
        ergebnis = float(zahl1 / zahl2)

    return ergebnis


endgültiges_ergebnis = berechne(
    float(input("zahl1:")), float(input("zahl2:")), (input("operator (+, -, *, /):"))
)
print(f"Ergebnis: {endgültiges_ergebnis}")
