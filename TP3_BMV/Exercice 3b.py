from time import sleep

nombre = int (input ("Choisissez un nombre: "))

for i in range (nombre, -1, -1) :
    print (i,flush=True)
    sleep(1)
