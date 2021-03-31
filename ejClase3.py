def cifradoCesar(phrase):
    ''' Recibe una frase y la convierte mediante el cifrado cesar '''    

    # Se incrementa mediante el map y una funcion lambda cada caracter ascii en 1
    aux_str = ''.join(map(lambda x: chr(ord(x) + 1), phrase))

    return aux_str


phrase = input('Ingrese una frase para realizar el cifrado \n')
print(f'La frase cifrada es {cifradoCesar(phrase)}')