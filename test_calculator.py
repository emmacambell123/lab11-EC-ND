# https://github.com/emmacambell123/lab11-EC-ND/tree/main
# Partner 1: Emma Campbell
# Partner 2: Nicholas De Faria

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    # Partner 2 tests

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)
        self.assertEqual(subtract(-2, -2), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(5, 25), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    # Partner 1 tests (left blank intentionally)

    # def test_multiply(self):
    #     pass

    # def test_divide(self):
    #     pass

    # def test_log_invalid_argument(self):
    #     pass

    # def test_hypotenuse(self):
    #     pass

    # def test_sqrt(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
