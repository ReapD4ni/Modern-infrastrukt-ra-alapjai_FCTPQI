import unittest
from src.calculator import Calculator

class TestCalculatorUnit(unittest.TestCase):

    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(3, 4), 12)

if __name__ == "__main__":
    unittest.main()
