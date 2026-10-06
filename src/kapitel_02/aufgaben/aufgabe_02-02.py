# Aufgabe 02-02
#  TODO: Ihre Lösung hier

personenzahl = input("Wie viele Personen teilen sich die Kosten?")
personenzahl = int(personenzahl)
geld = input("Wie hoch war die Rechensumme (in Euro)?")
geld = float(geld)
summe = geld // personenzahl
rest =
print(f" --- KOSTENAUFTEILUNG --- {\n }
Bei {personenzahl} Personen und einer Rechnungssumme von {geld} Euro: \n 
Jede Person zahlt mindestens {summe} Euro. \n
Es verbleibt ein Rest von {rest} Cent.")
