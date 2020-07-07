import unittest
import pytest

from calc import *

class Calc_Test(unittest.TestCase):

    simple_calc = Calc()

    def test_add(self):
        self.assertEqual(self.simple_calc.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(self.simple_calc.subtract(3, 1), 2)

    def test_multiply(self):
        self.assertEqual(self.simple_calc.multiply(3, 1), 3)

    def test_divide(self):
        self.assertEqual(self.simple_calc.divide(3, 3), 1)

    def cm_to_inches(self):
        self.assertEqual(self.simple_calc.cm_to_inches(25), 10)

    def cm_to_inches(self):
        self.assertEqual(self.simple_calc.cm_to_inches(50), 20)

    def test_modulo(self):
        self.assertTrue(self.simple_calc.modulo(50, 25))

    """
    
    Reverse engineering, here we are writing the test first
    before writing in the code file.
    """