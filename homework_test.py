import unittest
import math
import pytest


from homework import *

"""
We need to create a test class that inherits from
unittest.testcase, this gives us access to many unit testing
capabilites.

The method must start with test underscore in order for the module
to recognise the method.
"""

class Math_Test(unittest.TestCase):

    def test_find_sqrt(self):
        self.assertEqual(find_sqrt(81), 9)

    def test_find_ceil(self):
        self.assertEqual(find_ceil(27.8), 28)

