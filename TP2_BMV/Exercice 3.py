a=  input("Entrez la premiere (a)  valeur : ")
b=  input("Entrez la deuxieme (b) valeur : ")
c=  input("Entrez la troisieme (c) valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")
"""
 a= b+a
 b= b+c
 c= b-c
 b= b-c
 a= a-c 
 
 ou 
 
 a, b, c = b, c, a
"""

temp = a
a = b
b = c
c = temp


"""     *******************************************
         * Ne rien modifier apres cette ligne.
         *******************************************
"""

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)