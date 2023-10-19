#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
lista = []

def pedirListaDeNumeros() -> list:
    numero = -1
    while numero != 0:
        numero = int(input("Introduce un numero positivo: "))
        if numero.isDigit() and numero > 0:
            lista.append(numero)
    return lista


def obtenerNumeroMaximo(lista:list) -> int:
    return 0

def construirMensaje(numero: int) -> str:
    return ""


if __name__ == "__main__":
    #Entrada
    numeros = pedirListaDeNumeros()
    
    #Proceso
    maximo = obtenerNumeroMaximo(numeros)
    mensaje = construirMensaje(maximo)    
    
    #Salida
    print(mensaje)