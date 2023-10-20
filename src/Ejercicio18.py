#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
def pedirListaDeNumeros() -> list:
    lista = []
    numero = 0
    while numero != -1:
        try:
            numero = int(input("Introduce un numero positivo (-1 para terminar): "))
            if numero > 0:
                lista.append(numero)
            elif numero < -2:
                print("Introduce un número positivo.")
        except ValueError:
            print("Introduce un número válido.")
    return lista

def sumarNumeros(numeros):
    suma = 0
    while numeros > 0:
        digito = numeros % 10
        suma += digito
        numeros //= 10
    return suma

def contarPares(sumados):
    pares = 0
    for numero in sumados:
        if numero % 2 == 0:
            pares += 1
    return pares

def imprimirMensajeSuma(sumados) -> str:
    return "La suma de los numeros da: " + str(sumados)

def imprimirMensajePares(pares) -> str:
    return "Numero de pares introducidos: " + str(pares)

if __name__ == "__main__":
    #Entrada
    numeros = pedirListaDeNumeros()
    
    #Proceso
    sumados = sumarNumeros(numeros)
    pares = contarPares(numeros)
    #Salida
    mensajeSuma = imprimirMensajeSuma(sumados)
    print(mensajeSuma)
    mensajePares = imprimirMensajePares(pares)
    print(mensajePares)
