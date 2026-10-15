import random

Nessais = 0
x = random.randint(0, 100)
nombre = int (input ("Choisissez un nombre: "))

while x != nombre :
    if nombre < x :
        print("Le nombre cacher est plus grand")
        Nessais = Nessais + 1
    elif nombre > x :
        print("Le nombre cacher est plus petit")
        Nessais = Nessais + 1

    nombre = int (input ("Rechoisissez un nombre: "))

if nombre == x :
    print("Bien jouer! Vous avez trouver le nombre cacher en" , Nessais, "essais")