import sut
import unittest
import math
from unittest.mock import MagicMock

    def comparar(a, b):
        if a < b:
            return "A menor que B"
        if a > b:
            return "A mayor que B"
        if a == b:
            return "A y B son iguales"
