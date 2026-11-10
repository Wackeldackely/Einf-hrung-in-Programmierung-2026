# Aufgabe 06-05
#  TODO: Ihre Lösung hier

rollen_rechte = {
    "admin": {"lesen", "schreiben", "löschen", "benutzer_verwalten"},
    "editor": {"lesen", "schreiben"},
    "gast": {"lesen"},
}

rolle = input("Gib deine Rolle ein:").lower()
berechtigung = input("Welche Berechtigung wird benötigt?").lower()

print("Verfügbare Rollen: admin, editor, gast")
print(f"Gib deine Rolle ein: {rolle}")
print(f"Welche Berechtigung wird benötigt? {berechtigung}")

# for nutzer in rollen_rechte:
#   if rolle == "admin" in rollen_rechte:
#      if berechtigung in rollen_rechte"admin":
#         print(f"Zugriff gewährt: ein {rolle} darf {berechtigung}")

rechte_für_rolle = rollen_rechte.get(
    rolle, set()
)  # set() wenn jemand nacg etwas sucht, was nicht definiert ist dann gibt es none zurück
if berechtigung in rechte_für_rolle:
    print(f"Zugriff gewährt: Ein {rolle} darf {berechtigung}.")

else:
    print(f"Zugriff verweigert: Ein {rolle} darf nicht {berechtigung}.")
