# Aufgabe 02-01
#  TODO: Ihre Lösung hier

minutenzahl = input("Bitte gib die Anzahl der Minuten ein")
minutenzahl = int(minutenzahl)
# minutenzahl = int(input("Bitte))
stundenzahl = minutenzahl // 60
restzeit = minutenzahl % 60
print(
    f" {minutenzahl} Minuten entsprechen {stundenzahl} Stunden und {restzeit} Minuten"
)
