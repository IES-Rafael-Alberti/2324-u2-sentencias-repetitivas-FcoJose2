#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def comprobarContra(contraseña):
    while not (contraseña == "Prueba"):
        contraseña = input("Incorrecto. Vuelva a intentarlo: ")
    resultado = "Correcto"
    return resultado


if __name__ == "__main__":
    #Entrada
    contraseña = input("Introduzca su contraseña: ")
    #Proceso
    resultado = comprobarContra(contraseña)
    #Salida
    print(resultado)
