import unittest
from my_awesome_lib.math_tools import add, multiply

class TestMathTools(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

if __name__ == '__main__':
    unittest.main()
