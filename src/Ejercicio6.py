#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

def escalera(escalones):
    escalera = ""
    for i in range(1, escalones + 1):
        escalera += "*" * i +"\n"
    return escalera
    
if __name__ == "__main__":
    escalones = int(input("Cuantos escalones tendrá el triangulo rectangulo: "))
    resultado = escalera(escalones)
    print(resultado)