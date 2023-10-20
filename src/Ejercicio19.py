#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

def menuInicio():
    return "1-Comenzar programa\n2-Imprimir listado\n3-Finalizar programa\n"

def eleccion(opcion):
    while True:
        if opcion == "1":
            return "Inicio del programa"
        elif opcion == "2":
            return "Manzana\nPlatanos\nKiwis\nMelocotones\n"
        elif opcion == "3":
            break
        else:
            return "Opción incorrecta"
        

if __name__ == "__main__":
        print(menuInicio())
        opcion = input("Introduce una opción: ")
        act = eleccion(opcion)
