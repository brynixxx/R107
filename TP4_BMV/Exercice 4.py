L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 6, 9]
nb_values = len(L1)
max_nb_oc = 0
max_point = 0


for i in range(nb_values):
    point = L1[i]
    nb_oc = 0
    for n in L1 :
        if n == point:
            nb_oc += 1

    if nb_oc > max_nb_oc:
        max_nb_oc = nb_oc
        max_point = point

print(max_point, max_nb_oc)
