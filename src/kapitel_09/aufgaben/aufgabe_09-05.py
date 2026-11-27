# Aufgabe 09-05
#  TODO: Ihre Lösung hier

import pickle


class Spieler:
    def __init__(self, name, score):
        self.name = name
        self.score = score


with open("highscore.plk", "wb") as f:
    pickle.dump(Spieler, f)
