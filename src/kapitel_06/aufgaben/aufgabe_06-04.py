# Aufgabe 06-04
#  TODO: Ihre Lösung hier

bestellungen = [
    (101, "K-001"),
    (102, "K-002"),
    (103, "K-001"),
    (104, "K-003"),
    (105, "K-002"),
]
# (105, "K-002") => das ist eine "bestellung" (105)=> das ist eine einzigartige_kd
# einzigartige_k = { kundendaten for bestellung in bestellungen for kundendaten in bestellung}
# ist eine set comprehention

einzigartige_kd = set()
for bestellung in bestellungen:
    einzigartige_kd.add(bestellung[1])

print(einzigartige_kd)
print(f"Anzahl der eindeutigen Kunden: {len(einzigartige_kd)}")
