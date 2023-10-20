#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).




def añoscumplidos(edad):
    años = []
    for i in range(1, edad+1):
        años.append(i)
    return años


if __name__ == "__main__":
    #Entrada
    edad = int(input("Introduzca su edad: "))
    #Proceso
    años = añoscumplidos(edad)
    #Salida
    print(str(años))