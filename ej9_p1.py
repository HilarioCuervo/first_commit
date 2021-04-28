word = input('Ingrese una palabra \n')

# Se crea una lista con las letras de 'word' en minuscula y se quitan los espacios
list_of_letters = list(word.lower().replace(' ', ''))

# Se crea una variable boolean que va a tomar un valor de acuerdo a si la palabra es un heterograma
correct = True

for letter in list_of_letters:
    # Si 'letter' es una letra y aparece mas de una vez se pone en False la variable 'correct'
    if (letter.isalpha() and (list_of_letters.count(letter) > 1)):
        correct = False
        print(letter)
        break

# Se imprime si la palabra ingresada es un heterograma de acuerdo al valor de 'correct'
if (correct):
    print('La palabra es un Heterograma')
else:
    print('La palabra NO es un Heterograma')