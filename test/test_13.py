from src.Ejercicio13 import eco

def test_eco():
    assert eco("Prueba") == False
    assert eco("salir") == True