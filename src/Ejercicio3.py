#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def numerosImpar(numero):
    impar = []
    for i in range(1, numero+1, 2):
        impar.append(i)
    return impar

if __name__ == "__main__":
    numero = int(input("Introduce un numero: "))
    resultado = numerosImpar(numero)
    print(resultado)
