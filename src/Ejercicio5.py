
def inversion(cantidad, interes, tiempo):
    for i in range(tiempo):
        cantidad *= 1 + interes / 100
        print(f"Año {i + 1}: {cantidad:.2f}")
    return cantidad
        



if __name__ == "__main__":
    cantidad = float(input("Introduce la inversión inicial: "))
    interes = float(input("Introduce el interes: "))
    tiempo = int(input("Introduce durante cuantos años se va a invertir: "))

    cantidad = inversion(cantidad, interes, tiempo)
    print("Capital final después de " + str(tiempo) + "años: " + str(round(cantidad, 2)))