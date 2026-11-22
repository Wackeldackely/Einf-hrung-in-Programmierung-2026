# Aufgabe 08-03
#  TODO: Ihre Lösung hier


class Mitarbeiter:
    def __init__(self, name, gehalt):
        self.name = name
        self._gehalt = 0
        self.gehalt = gehalt
        return print(f"{self.name} hat ein Gehalt von {self.gehalt} Euro.")

    @property
    def gehalt(self):
        return self._gehalt

    @gehalt.setter
    def gehalt(self, wert):
        if isinstance(wert, (int, float)) and wert > 0:
            self._gehalt = wert
            print(f"Gehalt erfolgreich geändert auf {self._gehalt} ")

        else:
            print(
                "Fehler: Das Gehalt darf nicht negativ sein. Wert wurde nicht geändert."
            )

    def __str__(self):
        return f"{self.name} hat ein Gehalt von {self.gehalt} Euro."


mitarbeiter1 = Mitarbeiter("Anna", 50000)
mitarbeiter1.gehalt = 55000

print(mitarbeiter1)
print(f"{mitarbeiter1.name}s finales Gehalt: {mitarbeiter1.gehalt}")
