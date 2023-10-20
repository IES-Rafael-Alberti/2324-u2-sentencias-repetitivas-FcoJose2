#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tabla110():
    tabla = ""
    for i in range(1,11):
        for j in range(1,11):
            resultado = i * j
            tabla += f"{i} x {j} = {resultado}\n"
    return tabla


if __name__ == "__main__":
    #Entrada

    #Proceso
    resultado = tabla110()
    #Salida
    print(resultado)