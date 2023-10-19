#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def repetir(palabra):
    palabras = []
    for i in range(1,11):
        palabras.append(palabra)
    return palabras


if __name__ == "__main__":
    palabra = input("Escribe una palabra: ")
    resultado = repetir(palabra)
    print(resultado)
