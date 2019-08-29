import calculos
import unittest
import math
import sut
from unittest.mock import MagicMock

    def test_supercalc(self):
        math.exp=MagicMock(return_value=2)
        math.sqrt=MagicMock(return_value=2)
        a=sut.supercalc(3)
        self.assertTrue(a==2)
