# Aufgabe 03-02
#  TODO: Ihre Lösung hier
# wochentag = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
# wochenende = ["Samstag", "Sonntag"]

status = input("Welcher Wochentag ist heute?")

# if status.lower() in wochenende:
#   anstatt des anderen if befehls

if status == "Samstag" or status == "Sonntag":
    print("Schönes Wochenende!")

# elif status.lower() in wochentage:
#   print("Eine produktive Woche!")
# else:
#   print("Das ist kein Wochentag!")

else:
    print("Eine produktive Woche!")

# aber das Programm würde alles was eingegeben wird und weder Samstag noch Sonntag ist als ein wort erkennen, beidem es einem "eine produktive Woche" wünschen
