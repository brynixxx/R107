nombre = int(input("Choissisez un nombre/chiffre :"))

if (nombre < 0 and nombre % 2 == 0) :
    print("Le nombre est negatif et pair")
elif  (nombre < 0 and nombre % 2 != 0) :
    print("Le nombre est negatif et impair")
elif (nombre > 0 and nombre % 2 != 0) :
    print("Le nombre est positif et impair")
elif (nombre > 0 and nombre % 2 == 0) :
    print("Le nombre est positif et pair")
else : print("Le nombre est 0")
