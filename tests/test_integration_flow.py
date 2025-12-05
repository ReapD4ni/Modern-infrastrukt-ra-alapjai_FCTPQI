import unittest
from src.calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):

    def test_calculation_flow(self):
        calc = Calculator()
        result = calc.multiply(calc.add(1, 2), 5)
        self.assertEqual(result, 15)

if __name__ == "__main__":
    unittest.main()
