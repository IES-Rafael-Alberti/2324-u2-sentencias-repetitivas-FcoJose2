from src.Ejercicio16 import obtenerNumeroMaximo
from src.Ejercicio16 import construirMensaje


def test_obtenerNumeroMaximo():
    assert obtenerNumeroMaximo([1, 5, 3, 8, 2]) == 8
    assert obtenerNumeroMaximo([10, 0, 5, -3]) == 10
def test_construirMensaje():
    assert construirMensaje(7) == "El numero mas alto de la lista es 7"
    assert construirMensaje(0) == "El numero mas alto de la lista es 0"