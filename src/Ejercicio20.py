def buscarLetra(frase, letra):
    for i, caracter in enumerate(frase):
        if caracter == letra:
            return ("Se encontró la letra '" + str(letra) + "' en la posición " + str(i))
        
if __name__ == "__main__":
    frase  = input("Introduce una frase: ")
    letra = input("Introduce una palabra: ")

    mensaje = buscarLetra(frase, letra)

    print(mensaje)