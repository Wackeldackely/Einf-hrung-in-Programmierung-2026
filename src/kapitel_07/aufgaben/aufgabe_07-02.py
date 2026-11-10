# Aufgabe 07-02
#  TODO: Ihre Lösung hier


def erstelle_gruss(name: str, anrede: str = "Sehr geehrte/r", titel: str = "") -> str:
    if titel == "":
        gruss = anrede + " " + name + ","

    else:
        gruss = anrede + " " + titel + " " + name + ","

    return gruss


# ausdruck = erstelle_gruss(input("name:"), input("anrede:"), input("titel:"))
# print(ausdruck)
print(erstelle_gruss("Max Mustermann"))

print(erstelle_gruss("Ada Lovelace", "Hallo Frau", "Prof. Dr."))

print(erstelle_gruss("Peer Tester", "Guten Tag Heer"))
