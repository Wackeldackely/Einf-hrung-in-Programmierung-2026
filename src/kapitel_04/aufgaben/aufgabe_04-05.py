# Aufgabe 04-05
#  TODO: Ihre Lösung hier

# plus = "+"
# leerzeichen = " "
# for i in plus:
#   if leerzeichen <= 5:
#      print(leerzeichen * 5)

maß = 15

for y in range(maß):
    for x in range(maß):
        if 0 <= y <= 4 or 10 <= y <= 14:
            if 0 <= x <= 4 or 10 <= x <= 14:
                print(" ", end="")

            else:
                print("+", end="")

        elif 5 <= y <= 9:
            # if 0 <= x <= 14:
            print("+", end="")

    print(" ")
