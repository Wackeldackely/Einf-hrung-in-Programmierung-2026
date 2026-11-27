# Aufgabe 09-05
#  TODO: Ihre Lösung hier

import pickle


class Spieler:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self) -> str:
        return f"{self.name}: {self.score}"


    spieler_liste = []

    while True:
         name = input("Gib deinen Namen ein: ")
         if name == " ":
            break
        score = int(input("Gib deinen Score ein: "))

spieler_liste.append(Spieler(name, score))

with open("highscore.plk", "wb") as f:
    pickle.dump(Spieler, f)
    print("Highscore gespeichert!")


try:
    with open("highscore.plk", "rb") as f:
        Spieler_reloaded = pickle.load(f)

except FileNotFoundError as e:
    print(f"Ein Fehler ist aufgetreten: {type(e)}")
