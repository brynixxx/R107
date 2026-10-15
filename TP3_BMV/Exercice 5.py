nombre = int(input("Choissisez un nombre entier: "))
Resultat = 1
x= 0
n = 1

# for i in range (1, nombre+1):
#    i = i*Resultat
#    Resultat = i
#    print(Resultat)

while x != nombre:
    x = x+1
    x = x*Resultat
    Resultat = x
    print(Resultat)