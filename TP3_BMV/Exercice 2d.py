X = int(input("Entrer un nombre superieur a 1: "))
n = 0

if X < 1 :
    print("Le nombre est inferieur a 1, essayer encore!")
else :
    for i in range (0, X) :
        i = i+1
        X = X - i

        if X == 0 :
            print("Le plus grand nombre N est" ,i,)
            break
        elif X < 0 :
            n = X % i
            print("Le nombre maximum est", i-1, "mais il reste que" ,n, "sauf qu'il faut" ,i, "pour passer au nombre superieur")
            break