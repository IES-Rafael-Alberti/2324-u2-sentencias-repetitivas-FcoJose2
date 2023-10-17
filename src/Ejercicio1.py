#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def repetir(palabra):
    for i in range(1,11):
        print(palabra)
        i = i+1


if __name__ == "__main__":
    palabra = input("Escribe una palabra: ")
    repetir(palabra)
