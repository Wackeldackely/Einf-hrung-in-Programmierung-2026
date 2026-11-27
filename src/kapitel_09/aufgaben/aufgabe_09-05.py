# Aufgabe 09-05
#  TODO: Ihre Lösung hier

import pickle


class Spieler:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self) -> str:
        return f""


with open("highscore.plk", "wb") as f:
    pickle.dump(Spieler, f)
    print("Highscore gespeichert!")


try:
    with open("highscore.plk", "rb") as f:
        Spieler_reloaded = pickle.load(f)

except FileNotFoundError as e:
    print(f"Ein Fehler ist aufgetreten: {type(e)}")
