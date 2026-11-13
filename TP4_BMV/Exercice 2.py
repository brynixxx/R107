# Demande le nombre d'étudiants à l'utilisateur
from win32api import mouse_event

nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = [ ]
diff = [ ]

for i in range(nombreEtudiants):
    notes.append(int(input("Donnez la note de l'etudiant : ")))
    if notes[i] < 0 or notes[i] > 20:
        notes.remove(notes[i])
        notes.append(int(input("Ressayer de donner une note entre 0 et 20 : ")))
    else :
        moyenne = moyenne + notes[i]

moyenne = moyenne / nombreEtudiants

for i in range(nombreEtudiants):
    diff.append(notes[i] - moyenne)

print("Le nombre d'etudiants est de :", nombreEtudiants)

for i in range(nombreEtudiants):
    print("Note etudiant", i, ":", notes[i])

print("La moyenne de la classe est : ", moyenne)

print("Numero de l'etudiant | note | ecart de la moyenne")

for i in range(nombreEtudiants):
    print(i, "|", notes[i], "|", diff[i],)

