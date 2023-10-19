#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

def sumatorioPositivo(numero, suma):
    suma = 0
    while numero != 0:
        if numero > 0:
            suma = suma + numero
        else:
            print("No se permiten numeros negativos.")
            break
        numero = int(input("Introduzca un numero positivo: "))
        
    return suma

if __name__ == "__main__":
    #Entrada
    numero = int(input("Introduce un numero positivo: "))
    suma = 0
    #Proceso
    resultado = sumatorioPositivo(numero, suma)
    #Salida
    print(resultado)