import csv

archivo = open('appstore_games.csv', 'r', encoding = 'utf-8')
arch_reader = csv.reader(archivo, delimiter = ',')

next(arch_reader)

juegos_español = []
ratings = []

for game in arch_reader:
    if ('ES' in game[12]) and (game[7] == '0'):
        juegos_español.append(game[2])
    try:
        ratings.append(int(game[6].replace("'","")))
    except ValueError:
        pass

print('Juegos gratis en español:')
for game in juegos_español:
    print(game)


ratings = sorted(ratings, key = lambda rate: rate, reverse = True)

print('Los 10 mejores calificados:')
for i in range(0,10):
    print(ratings[i])
   

