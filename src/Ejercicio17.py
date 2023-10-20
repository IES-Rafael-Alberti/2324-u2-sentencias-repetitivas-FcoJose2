#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.


def obtenerNumero() -> int:
    try:
        numero = int(input("Introduce un numero positivo: "))
        if numero < 0:
            print("Introduce un número positivo.")
    except ValueError:
        print("Introduce un número válido.")
    return numero

def separarNumero(numero:int) -> list:
    resultado = list(map(int,str(numero)))
    return resultado

def sumarNumeros(numerosSeparados:list) -> int:
    total = 0
    for i in numerosSeparados:
       total = total+i
    return total

def imprimirMensaje(numerosSumados:int) -> str:
    return "En total los numeros introducidos son: "+ str(numerosSumados)

if __name__ == "__main__":
    #Entrada
    numero = obtenerNumero()
    #Procesar
    numerosSeparados = separarNumero(numero)
    numerosSumados = sumarNumeros(numerosSeparados)
    #Salida
    mensaje = imprimirMensaje(numerosSumados)
    print(mensaje)

