# Aufgabe 07-03
#  TODO: Ihre Lösung hier


def noten_statistik(*noten: float) -> dict:
    # *noten = *args => das heißt unendlich viele argumente/parameter in der funktion
    if noten:  #!= None:
        beste = min(noten)
        schlechteste = max(noten)
        durchschnitt = sum(noten) / len(noten)
        statistik = {
            "beste_note": beste,
            "schlechteste_note": schlechteste,
            "durchschnitt_note": durchschnitt,
        }
        return statistik

    else:
        # noten == None
        statistik = {
            "beste_note": None,
            "schlechteste_note": None,
            "durchnittliche_note": 0.0,
        }
        return statistik


print(f"Statistik 1: {noten_statistik(1.0, 1.3, 2.0, 4.0, 2.7, 2.5)}")

print(f"Statistik 2: {noten_statistik(2.3)}")

print(f"Statistik 3: {noten_statistik()}")
