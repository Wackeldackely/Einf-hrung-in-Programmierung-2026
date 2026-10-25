# Aufgabe 04-02
#  TODO: Ihre Lösung hier

zahlen = range(1, 101)

for zahl in zahlen:
    if zahl % 3 == 0 and zahl % 5 == 0:
        print("FizzBuzz")

    elif zahl % 5 == 0:
        print("Buzz")

    elif zahl % 3 == 0:
        print("Fizz")

    else:
        print(zahl)
