#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def inverso(palabra):
    for i in range(len(palabra)-1, -1, -1):
        print(palabra[i])
    
if __name__ == "__main__":
    palabra = input("Introduce una palabra: ")
    inverso(palabra)
