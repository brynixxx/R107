i = 0
x = 0  # Inférieur strictement a 10
y = 0  # Supérieur ou égale a 10 et inférieur strictement a 15
z = 0  # Supérieur ou égale a 15

while i != 10 :
    nombre = int (input("Entrer un nombre: "))
    if  nombre < 10 :
        x = x + 1
    elif nombre >= 10 and nombre < 15 :
        y = y + 1
    else :
        z = z + 1
    i = i + 1

print("Le nombre de valeurs inferieures a 10 est :" , x,)
print("Le nombre de valeurs superieures ou egale a 10 et inferieures strictement a 15 est : " ,y,)
print("Le nombre de valeurs superieures ou egale a 15 est : " ,z,)