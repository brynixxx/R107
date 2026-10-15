BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Quelle est le nombre de convives ? :"))

NVQfromage = fromage*nbConvives / BASE
NVQeau = eau*nbConvives / BASE
NVQail = ail*nbConvives / BASE
NVQpain = pain*nbConvives / BASE

print('Pour faire une fondue fribourgeoise pour ', nbConvives , ' personnes, il vous faut :')
print(NVQfromage)
print(NVQeau)
print(NVQail)
print(NVQpain)

