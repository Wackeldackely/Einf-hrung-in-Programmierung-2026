# Aufgabe 04-06

# import random
# import string

# Nützliche Zeichenketten aus dem string-Modul holen.
# Alternativ könnten wir sie auch selbst definieren: klein = "abc..."
# KLEINBUCHSTABEN = string.ascii_lowercase
# GROSSBUCHSTABEN = string.ascii_uppercase
# ZAHLEN = string.digits
# SONDERZEICHEN = string.punctuation

# Tipps:
# print(SONDERZEICHEN)

# experimentiere hier mehrfach mit SHIFT+ENTER
# print(random.choice(SONDERZEICHEN))

#  TODO: Deine Lösung hier:
import random
import string

KLEINBUCHSTABEN = string.ascii_lowercase
GROSSBUCHSTABEN = string.ascii_uppercase
ZAHLEN = string.digits
SONDERZEICHEN = string.punctuation

kbanzahl = int(input("Anzahl Kleinbuchstaben"))
gbanzahl = int(input("Anzahl Großbuchstabe"))
number = int(input("Anzahl Zahlen"))
szanzahl = int(input("Anzahl Sonderzeichen"))

passwort = []

for x in range(kbanzahl):
    neukb = random.choice(KLEINBUCHSTABEN)
    passwort.append(neukb)

for x in range(gbanzahl):
    neugb = random.choice(GROSSBUCHSTABEN)
    passwort.append(neugb)

for x in range(number):
    neunumber = random.choice(ZAHLEN)
    passwort.append(neunumber)

for x in range(szanzahl):
    neusz = random.choice(SONDERZEICHEN)
    passwort.append(neusz)

random.shuffle(passwort)
liste = "".join(passwort)

print(
    f"--- Passwort-Generator --- \n \n Anzahl Kleinbuchstaben: {kbanzahl} \n Anzahl Großbuchstaben: {gbanzahl} \n Anzahl Zahlen: {number} \n Anzahl Sonderzeichen: {szanzahl} \n"
)

print(f"Dein zufälliges Passwort lautet: {liste}")
