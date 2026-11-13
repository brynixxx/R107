nMax = 3
v1 = [ ]
v2 = [ ]
ps = 0

n = int(input("Choissisez la taille de votre vecteur : "))

if n > nMax:
    n = int(input("La taille de votre vecteur doit etre entre 1 et 3"))
else :
    for i in range(n):
        v1.append(int(input("Choissisez votre composante du vecteur 1 :")))
        v2.append(int(input("Choissisez votre composante du vecteur 2 :")))

for i in range(n):
    ps = ps + (v1[i] * v2[i])

print("La taille du vecteur est de : ", n)

print("Saisie du premier vecteur : ")
for i in range(n):
    print("v1[", i, "] = ", v1[i] )

print("Saisie du deuxieme vecteur : ")
for i in range(n):
    print("v2[", i, "] = ", v2[i] )

print("Le produit scalaire de v1 par v2 vaut :", ps)