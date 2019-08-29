import unittest


class TestSimple(unittest.TestCase):
    def test_simple1(self):

        self.assertEqual(2, 2)

    def test_simple2(self):
        self.assertIn(1, [4, 5])

    def test_simple3(self):
        self.assertLess(8, 9)  #menor


if __name__ == '__main__':
    unittest.main()

'''
se ejecuto y dio:  Ran 3 tests in 0.001s
test_simple1 (__main__.TestSimple) ... ok  lo paso y dio assert
test_simple2 (__main__.TestSimple) ... FAIL  no paso el assert no puede sumar una lista
test_simple3 (__main__.TestSimple) ... ok  lo paso, 8 es menor
'''
