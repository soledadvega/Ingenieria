from unittest.mock import MagicMock

#test
def test_costototal(self):
    sut.sumar=MagicMock(return_value=2)
    total = sumar(producto1, producto2)
    return "El costo total es $" + str(total)
