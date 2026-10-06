# Aufgabe 02-03
#  TODO: Ihre Lösung hier
# nur  * ist einfach nur normales multiplizieren

anfangskapital = input("bitte gib das Anfangskapital in Euro ein:")
anfangskapital = int(anfangskapital)
zinssatz = input("Bitte gib den inssatz in Prozent an:")
zinssatz = int(zinssatz)
p = float(zinssatz / 100)
zeit = input("Bitte gib die Laufzeit in Jahren ein")
zeit = int(zeit)
K = float(anfangskapital * (1 + p) ** zeit)

print(
    f"--- ZINSRECHNER --- \n Anfangskapital: {anfangskapital} \n Euro Zinssatz: {zinssatz}% \n Laufzeit: {zeit} Jahre \n \n Nach 10 Jahren beträgt das Endkapital: {K} Euro."
)
