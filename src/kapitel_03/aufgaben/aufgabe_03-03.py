# Aufgabe 03-03
#  TODO: Ihre Lösung hier

bestellung = float(input("Bitte geben Sie den Bestellwert ein:"))
vip = input("Sind Sie Premium-Mitglied (ja/nein)?")


if vip == "nein":
    if bestellung >= 50:
        versandkosten = 0

    elif bestellung < 50:
        versandkosten = 4.99


elif vip == "ja":
    versandkosten = 0

g_kosten = float(bestellung + versandkosten)

print(
    f"--- VERSANDKOSTEN-RECHNER --- \n Bestellwert:   {bestellung} Euro \n Versandkosten: {versandkosten} Euro \n \n Gesamtbetrag:    {g_kosten:.2f} Euro "
)
