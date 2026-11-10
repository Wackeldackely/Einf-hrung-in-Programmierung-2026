# Aufgabe 05-05
#  TODO: Ihre Lösung hier

adressen = [
    "test@example.com",
    "user.name@domain.co",
    "user@localhost",
    "no-at-sign.com",
    "user@.com",
    "@domain.com",
]

akt_emails = []

print(f"Ursprüngliche Liste: {adressen}")

for user in adressen:
    if user.count("@") == 1 and user.find(".") > user.find("@"):
        akt_emails.append(user)

print(f"Gültige E-Mail-Adressen: {akt_emails}")
