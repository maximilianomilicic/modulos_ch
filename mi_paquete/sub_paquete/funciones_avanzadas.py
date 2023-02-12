def contar_letras(frase):
    numeros_letras = 0
    for l in frase:
        if l != ' ':
            numeros_letras += 1
    return numeros_letras