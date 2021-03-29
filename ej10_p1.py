# Diccionario para almacenar los valores de cada letra
dict_of_score = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'], 4: ['F', 'H', 'V', 'W', 'Y'], 5: ['K'], 8: ['J', 'X'], 10: ['Q', 'Z']}

word = input('Ingrese una palabra \n')

# Se crea una lista con las letras en mayuscula de la palabra ingresada 
list_of_letters = list(word.upper())

# Variable para almacenar el puntaje
score = 0

# Se recorre para cada letra de 'list_of_letters' el diccionario
for letter in list_of_letters:
    # Si letter no es una letra directamente no la busca
    if letter.isalpha():
        for elem in dict_of_score:
            # Si encuentra una coincidencia incrementa 'score' con el valor de la key donde encontro la letra
            if letter in dict_of_score[elem]:
                score += elem
                break

print(score)