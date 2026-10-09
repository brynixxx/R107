jour = int(input('Entrez le nombre de jours depuis le debut du mois : '))
heure = int(input('Entrez le nombre de heures depuis le debut du mois : '))
minute = int(input('Entrez le nombre de minutes depuis le debut du mois : '))

minutej = jour*1440
minuteh = heure*60
minuteT = minutej + minuteh + minute
print('Le nombre total de minute depuis le debut du mois est de' , minuteT , 'minutes')