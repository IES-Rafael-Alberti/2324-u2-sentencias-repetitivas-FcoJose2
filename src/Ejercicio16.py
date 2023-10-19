#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
lista = []
def numeroMaximo(numero):
    
    while numero != 0:
        lista.append(numero)
        numero = int(input("Introduce un numero positivo: "))
    return max(lista)


if __name__ == "__main__":
    #Entrada
    numero = int(input("Introduce un numero positivo: "))
    #Proceso
    resultado = numeroMaximo(numero)
    #Salida
    print(resultado)