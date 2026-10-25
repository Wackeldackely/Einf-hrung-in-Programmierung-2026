# Aufgabe 04-01
#  TODO: Ihre Lösung hier

import random

zufallszahl = random.randint(1, 100)
guess = int(input("Dein Tipp für die zufallszahl:"))
tries = 1

print("--- Zahlenratespiel ---")
print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Rate mal!")

while zufallszahl != guess:
    print(f"Dein Tipp: {guess}")

    if zufallszahl < guess:
        print("Zu hoch! Versuche es nochmal")

    elif zufallszahl > guess:
        print("Zu niedrig! Versuche es nochmal")

    guess = int(input("Dein Tipp für die zufallszahl:"))
    tries += 1

print(f"Korrekt! Du hast die Zahl {zufallszahl} in {tries} Versuchen erraten!")
