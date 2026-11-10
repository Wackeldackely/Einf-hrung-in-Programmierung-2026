# Aufgabe 06-03
#  TODO: Ihre Lösung hier

python_kurs = ["Anna", "Ben", "Clara", "David"]
db_kurs = ["Clara", "David", "Eva", "Frank"]
nur_python = set(python_kurs)
nur_db = set(db_kurs)

beide = nur_python & nur_db
ohne = nur_python - nur_db

print(f"Studierende in beiden Kursen: {beide} \nStudierende nur im Python-Kurs: {ohne}")
