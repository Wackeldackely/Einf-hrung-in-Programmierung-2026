# Aufgabe 09-01
#  TODO: Ihre Lösung hier

import datetime

# oder: datetime import datetime datetime damit man nicht modulname.klassenname.eingabe schreiben muss
# jetzt = datetime.datetime.now() ist so nicht nötigt, da sinst immer der gleiche zeitstempel herrscht

while True:
    text = input("Logbucheintrag oder exit eingeben: ")
    if text == "exit":
        break

    else:
        with open("logbuch.txt", "a", encoding="utf-8") as f:
            neuer_eintrag = f"{datetime.datetime.now()} - {text}\n"
            f.write(neuer_eintrag)

        with open("logbuch.txt", "r", encoding="utf-8") as f:
            zeilen = f.readlines()
            print(f"{datetime.datetime.now()} - {text} \n")
