#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
lista = []

def pedirListaDeNumeros() -> list:
    numero = -1
    while numero != 0:
        try:
            numero = int(input("Introduce un numero positivo (0 para terminar): "))
            if numero > 0:
                lista.append(numero)
            elif numero < 0:
                print("Introduce un número positivo.")
        except ValueError:
            print("Introduce un número válido.")
    return lista


def obtenerNumeroMaximo(lista:list) -> int:
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero

    return maximo


def construirMensaje(maximo: int) -> str:
    return "El numero mas alto de la lista es " + str(maximo)


if __name__ == "__main__":
    #Entrada
    numeros = pedirListaDeNumeros()
    
    #Proceso
    maximo = obtenerNumeroMaximo(numeros)
    mensaje = construirMensaje(maximo)    
    
    #Salida
    print(mensaje)