#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def repetir(palabra):
    palabras = []
    for i in range(1,11):
        palabras.append(palabra)
    return palabras


if __name__ == "__main__":
    #Entrada
    palabra = input("Escribe una palabra: ")
    #Proceso
    resultado = repetir(palabra)
    #Salida
    print(resultado)
