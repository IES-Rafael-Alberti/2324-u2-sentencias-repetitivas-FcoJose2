#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def cuentaAtras(numero):
    lista = []
    for i in range(numero, -1, -1):
        lista.append(i)
    return lista


if __name__ == "__main__":
    #Entrada
    numero = int(input("Introduce un numero: "))
    #Proceso
    resultado = cuentaAtras(numero)
    #Salida
    print(resultado)