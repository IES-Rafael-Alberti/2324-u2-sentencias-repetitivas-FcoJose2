from src.Ejercicio4 import cuentaAtras

def test_cuentaAtras():
    assert cuentaAtras(20) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]