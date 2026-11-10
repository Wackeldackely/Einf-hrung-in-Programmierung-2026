# Aufgabe 07-05
#  TODO: Ihre Lösung hier
#
# def filter_mitarbeiter(mitarbeiter_liste: list[dict], **kriterien) -> list[dict]:
# gefilterte_liste = mitarbeiter_liste[:]

# `kriterien` is ein dict
#
# print(kriterien)
# for kriterium, wert in kriterien.items():
#   gefilterte_liste = list(filter(
#      lambda m: m.get(kriterium, "unbekannt") == wert
#     , gefilterte_liste))
# return gefilterte_liste

# filter_mitarbeiter(mitarbeiter, abteilung="IT", jahre_im_unternehmen=2)

# %%
mitarbeiter = [
    {"name": "Anna", "abteilung": "IT", "jahre_im_unternehmen": 5},
    {"name": "Ben", "abteilung": "Marketing", "jahre_im_unternehmen": 2},
    {"name": "Clara", "abteilung": "IT", "jahre_im_unternehmen": 8},
    {"name": "David", "abteilung": "IT", "jahre_im_unternehmen": 2},
]
# .items() gibt eine ansicht aller Schlüssel-Wert-Paare als Tupel zurück


def filter_mitarbeiter(mitarbeiter_liste: list[dict], **kriterien) -> list[dict]:
    gefilterte_liste = mitarbeiter_liste
