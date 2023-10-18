

def escaleraNumeros(numero):
    impar = ""
    for i in range(1, numero+1, 2):
        for j in range(i, 0, -2):
            print(j, end=" ")
        print(" ")
    return impar

if __name__ == "__main__":
    numero = int(input("Introduce un numero: "))
    resultado = escaleraNumeros(numero)
    print(resultado)

