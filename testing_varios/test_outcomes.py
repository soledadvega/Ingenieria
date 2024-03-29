import unittest


class TestOutcomes(unittest.TestCase):
    def test_1(self):
        a = "probando"
        self.assertIs(a, a)  #ok

    def test_2(self):
        self.assertListEqual([4, 5, 2], [4, 5])  #fail son listas dif

    def test_3(self):
        self.assertLess(8 / 0, 100)   #error, no se divide x cero

    def test_4(self):
        a = "5"
        b = [4]
        c = a - b
        self.assertEqual(c, 1)  #error de tipo:(string y lista)


if __name__ == '__main__':
    unittest.main()
