from src.Ejercicio20 import buscarLetra

def test_buscarLetra():
    assert buscarLetra("hola y adios", "y") == "Se encontró la letra 'y' en la posición 5"
