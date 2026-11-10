# Aufgabe 05-04
#  TODO: Ihre Lösung hier

netto_preise = [99.99, 14.50, 42.00, 120.55]

brutto_preise = [round(preis * 1.19, 2) for preis in netto_preise]

print(
    f"Netto-Preise: {netto_preise} \n Brutto-Preis (inkl. 19% MWst.): {brutto_preise}"
)
