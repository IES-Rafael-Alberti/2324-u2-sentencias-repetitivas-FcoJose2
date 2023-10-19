#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
lista = []
def numeroMaximo(numero):
    
    while numero != 0:
        lista.append(numero)
        numero = int(input("Introduce un numero positivo: "))
    return lista


if __name__ == "__main__":
    numero = int(input("Introduce un numero positivo: "))
    resultado = numeroMaximo(numero)
    print(max(resultado))