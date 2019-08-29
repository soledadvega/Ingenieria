import unittest
import sut

class TestSut(unittest.TestCase):


    def test_area(self):
        area = sut.area(3, 2)
        self.assertTrue(area==6)

    def test_sumar(self):
        resultado = sut.sumar(2, 3)
        self.assertTrue(resultado==5)

    def test_saludar(self):
        resultado = sut.saludar("Luz")
        self.assertTrue("Hola" + "Luz")

    def test_multiplicar(self):
        resultado = sut.multiplicar(2, 4)
        self.assertTrue(resultado==8)

    def test_valorabsoluto(self):
        resultado = sut.valorabsoluto(-5)
        self.assertTrue(resultado==5)


    def test_productoria(self):
        resultado = sut.productoria([1, 2, 3, 4, 5],3)
        self.assertTrue(resultado==6)


    def test_sumatoria(self):
        resultado = sut.sumatoria([1, 2, 3, 4, 5],3)
        self.assertTrue(resultado==6)



    def test_comparar(self):
        if a < b:
            return "A menor que B"
        if a > b:
            return "A mayor que B"
        if a == b:
            return "A y B son iguales"

    def test_costototal(self):
        resultado = sut.costototal()
        self.asserTrue(resultado== "El costo total es $2")
        total = sumar(producto1, producto2)
        return "El costo total es $" + str(total)


    def test_supercalc(self):
        exp = math.exp(num)
        sum = exp + 2
        sqrt = math.sqrt(sum)
        resultado = sut.supercalc()
        self.assertTrue(resultado == )
        return sqrt


if __name__ =="__main__":
    unittest.main()


'''
    def test_sumatoria(self):
        resultado = sut.sumatoria()
        self.assertTrue(resultado==  )

    def test_productoria(self):
        resultado = sut.productoria()
        self.assertTrue(resultado== )
'''
