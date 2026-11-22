# Aufgabe 08-04
#  TODO: Ihre Lösung hier


class Mitglied:  # n seite der beziehung
    def __init__(self, name):  # , team):
        self.name = name
        self.team = None

    def __str__(self) -> str:
        return self.name


class Team:  # 1 seite der beziehung
    def __init__(self, team_name):
        self.team_name = team_name
        self.mitglied = []

    def add_mitglied(self, mitglied):
        self.mitglied.append(mitglied)
        mitglied.team = self  # verknüfung zur klasse mitglied

    # def show_mitglieder(self):  # Gehört ins Team, da ein Team mehrere Mitglieder hat

    # def __str__(self) -> str:
    # return f"Team: {self.team_name}: {self.mitglied}"

    def show_mitglieder(self):  # Gehört ins Team, da ein Team mehrere Mitglieder hat
        for m in self.mitglied:
            print(f"- {m.name} \n")

        def __str__(self) -> str:
            # Wandelt die Objekte in der Liste in Namen um
            namen = ", ".join(m.name for m in self.mitglied)
            return f"Team: {self.team_name}: {namen}"

    # mitglieder = [ana, bob, clara]
    # oder: print("\n.join(map(lambda m: f"- {m}", mitglieder"))")


team1 = Team("Die Entwickler")
team1.add_mitglied(Mitglied("Anna"))
team1.add_mitglied(Mitglied("Ben"))
team1.add_mitglied(Mitglied("Clara"))
print(team1)
