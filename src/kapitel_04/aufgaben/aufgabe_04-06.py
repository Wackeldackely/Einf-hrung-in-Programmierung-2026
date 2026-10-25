# Aufgabe 04-06

import random
import string

# Nützliche Zeichenketten aus dem string-Modul holen.
# Alternativ könnten wir sie auch selbst definieren: klein = "abc..."
KLEINBUCHSTABEN = string.ascii_lowercase
GROSSBUCHSTABEN = string.ascii_uppercase
ZAHLEN = string.digits
SONDERZEICHEN = string.punctuation

# Tipps:
print(SONDERZEICHEN)

# experimentiere hier mehrfach mit SHIFT+ENTER
print(random.choice(SONDERZEICHEN))

#  TODO: Deine Lösung hier:

kbanzahl = int(input("Anzahl Kleinbuchstaben"))
gbanzahl = int(input("Anzahl Großbuchstabe"))
number = int(input("Anzahl Zahlen"))
szanzahl = int(input("Anzahl Sonderzeichen"))

for x in range(kbanzahl):
    neukb = random.choice(KLEINBUCHSTABEN)

for x in range(gbanzahl):
    neugb = random.choice(GROSSBUCHSTABEN)

for x in range(number):
    neunumber = random.choice(ZAHLEN)

for x in range(szanzahl):
    neusz = random.choice(SONDERZEICHEN)

passwort = []
