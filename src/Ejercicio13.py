#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def eco():
    while True:
        frase = input("-->")
        if frase == "salir":
            break
        print(frase)

eco()