L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
nb_values = len(L1)

for i in range(nb_values):
    point = L1[i]
    nb_oc = 0
    for n in L1:
        if n == point:
         nb_oc += 1

for i in range(0, nb_values, -1):
    if i == nb_oc :
        break

print(point, nb_oc)
