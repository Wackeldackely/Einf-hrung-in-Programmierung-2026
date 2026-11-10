# Aufgabe 06-02
#  TODO: Ihre Lösung hier
import string

SONDERZEICHEN = string.punctuation


satz = "Python ist super! Ja, wirklich super.".lower()

for sz in SONDERZEICHEN:
    satz = satz.replace(sz, "")

satz_geteilt = satz.split(" ")
# den satz genommen und von einer zeichenkette in die wörter aufgeteilt


vorkommen = {}  # strichliste an der anzahl der jeweiligen wörter

for wort in satz_geteilt:
    if wort not in vorkommen:
        vorkommen[wort] = 1
    else:
        vorkommen[wort] += 1

print("Häufigkeit der Wörter:")
for (
    wort,
    anzahl,
) in vorkommen.items():  # wort und anzahl sind temporäre variablen in vorkommen, denn items(schlüssel(wort), wert(anzahl)), aber nur bei Tupeln oder sequenzen
    print(f"- {wort}: {anzahl}")
