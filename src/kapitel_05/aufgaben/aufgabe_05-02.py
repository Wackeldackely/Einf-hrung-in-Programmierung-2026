# Aufgabe 05-02
#  TODO: Ihre Lösung hier

verkaufszahlen = [12, 15, 13, 18, 19, 22, 21, 20, 23, 25, 24, 27]

sortiert = sorted(verkaufszahlen)

print(f"Die drei umsatzstärksten Monate hatten Verkäufe von: {sortiert[-3:]}")

# q1 = sum(verkaufszahlen[:3])

# q2 = sum(verkaufszahlen[4:7])

# q3 = sum(verkaufszahlen[7:10])

# q4 = sum(verkaufszahlen[10:])

# qvergleich = [q1, q2, q3, q4]
# qvergleich.sort()

# print(f"Das beste Quartal war das {qvergleich[3]}. Quartal.")

bestesq = 0
gesamtu = []

for qstart in range(0, 12, 3):
    verkaufszahlen[qstart : qstart + 3]
    sum(verkaufszahlen[qstart : qstart + 3])
    bestesq += 1
    gesamtu.append(sum(verkaufszahlen[qstart : qstart + 3]))
print(f"Das beste Quartal war das {bestesq}. Quartal")

gesamtu.sort()

print(f" Gesamtumsatz im besten quartal: {gesamtu[3]}")
