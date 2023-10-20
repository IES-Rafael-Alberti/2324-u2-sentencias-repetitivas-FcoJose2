from src.Ejercicio17 import separarNumero, imprimirMensaje, sumarNumeros

def test_separarNumero():
    assert separarNumero(123) == [1, 2, 3]

def test_sumarNumeros():
    assert sumarNumeros([1, 2, 3]) == 6

def test_imprimirMensaje():
    assert imprimirMensaje(10) == "En total los numeros introducidos son: 10"