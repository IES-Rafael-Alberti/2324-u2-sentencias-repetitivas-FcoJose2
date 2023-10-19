#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

def sumatorio(numero, suma):
    suma = 0
    while numero != 0:
        suma = suma + numero
        numero = int(input("Introduzca un numero: "))
        
    return suma

if __name__ == "__main__":
    numero = int(input("Introduce un numero: "))
    suma = 0
    resultado = sumatorio(numero, suma)
    print(resultado)

