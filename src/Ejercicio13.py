#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def eco(entrada):
   return entrada == "salir"

if __name__ == "__main__":
   entrada = input("Escriba algo (escriba 'salir' para salir): ")

   while not eco(entrada):
      print(entrada)

      entrada = input("Escriba algo (escriba 'salir' para salir): ")