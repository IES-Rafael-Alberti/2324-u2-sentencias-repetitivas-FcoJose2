#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def contarLetras(frase, letra):
    contador = 0
    for i in frase:
        if i == letra:
            contador = contador + 1
    return contador


if __name__ == "__main__":
    frase = input("Introduzca una frase: ")
    letra = input("Introduzca una letra: ")
    contador = contarLetras(frase, letra)
    print(contador)
