minutes = int(input('Combien de minutes depuis le debut du mois? :'))


jour = minutes // 1440
heures = jour % 1440
minutesr = heures % 60

print('Jour:' , jour)
print('Heures:' , heures)
print('Minutes:' , minutesr)