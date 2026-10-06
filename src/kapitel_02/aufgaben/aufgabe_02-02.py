# Aufgabe 02-02
#  TODO: Ihre Lösung hier

personenzahl = input("Wie viele Personen teilen sich die Kosten?")
personenzahl = int(personenzahl)
geld = input("Wie hoch war die Rechensumme (in Euro)?")
geld = float(geld)
summe = geld // personenzahl
rest = geld % personenzahl
print(
    f" ---Kostenaufteilung---  Bei {personenzahl} Personen und einer Rechnungssumme von {geld} Euro:  Jede Person zahlt mindestens {summe} Euro. Es verbleibt ein Rest von {rest} Cent."
)
