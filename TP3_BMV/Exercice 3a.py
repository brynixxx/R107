from time import sleep


nombre = int (input ("Choissisez un nombre entier positif: "))

while nombre != 0 :
    sleep(1)
    nombre = nombre - 1
    print(nombre,flush=True)
