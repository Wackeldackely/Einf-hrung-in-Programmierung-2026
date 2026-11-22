# Aufgabe 08-02
#  TODO: Ihre Lösung hier


class Bankkonto:
    def __init__(self, inhaber, kontostand):
        self.inhaber = inhaber
        self.kontostand = kontostand
        # die in init festgelegten attribute kann man im verlauf überschreiben und dann mit diesen werten weiter arbeiten, keine neue variable erstellen!!!!
        return print(
            f"Neues Konto für {self.inhaber} mit {self.kontostand} Euro eröffnet."
        )

    def einzahlen(self, betrag):
        if isinstance(betrag, (int, float)):  # and 0 <= betrag:
            self.kontostand = self.kontostand + betrag

        return print(f"Kontostand nach Einzahlung: {self.kontostand}")

    def abheben(self, betrag2):
        if isinstance(betrag2, (int, float)) and 0 <= betrag2 <= self.kontostand:
            self.kontostand = self.kontostand - betrag2
            return print(f"Abhebung erfolgreich. Neuer Kontostand: {self.kontostand}")

        else:
            return print("Warnung: Abhebung nicht möglich. Kontostand zu gering.")


konto1 = Bankkonto("Max Musterman", 1000)
konto1.einzahlen(200)
konto1.abheben(500)
konto1.abheben(900)

print(f"Finaler Kontostand: {konto1.kontostand}")
