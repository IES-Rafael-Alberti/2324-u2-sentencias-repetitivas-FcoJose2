#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.


def primoOno(numero):
    primo = True
    for i in range(2, numero):
        if (numero % i) == 0:
            primo = False
    return primo

if __name__ == "__main__":
    numero = int(input("Introduzca un numero: "))
    primo = primoOno(numero)
    if primo == False:
        print("No es primo.")
    else:
        print("Es primo.")