# https://github.com/emmacambell123/lab11-EC-ND/tree/main
# Partner 1: Emma Campbell
# Partner 2: Nicholas De Faria

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    ######### Partner 2 tests #########
    # (from Partner 2 instructions: test_add, test_subtract,
    #  test_divide_by_zero, test_logarithm, test_log_invalid_base)

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
            div(10, 0)

    def test_logarithm(self):
        # log_10(1000) = 3
        self.assertAlmostEqual(logarithm(10, 1000), 3.0)
        # log_2(8) = 3
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        # log_5(25) = 2
        self.assertAlmostEqual(logarithm(5, 25), 2.0)

    def test_log_invalid_base(self):
        # base <= 0 or base == 1 should raise ValueError
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    ######### Partner 1 tests #########
    # (from Partner 1 instructions: test_multiply, test_divide,
    #  test_log_invalid_argument, test_hypotenuse, test_sqrt)

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 5), -5)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(10, 2), 5.0)
        self.assertAlmostEqual(div(-9, 3), -3.0)
        self.assertAlmostEqual(div(7, 2), 3.5)

    def test_log_invalid_argument(self):
        # invalid argument (b <= 0) should raise ValueError
        with self.assertRaises(ValueError):
            logarithm(10, 0)
        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(0, 7), 7.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(4), 2.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-1)


# NOTE: Lab’s Lab10/Lab11 runner imports this module and builds a test suite,
# so we don’t need to (and shouldn’t) print anything custom here.
if __name__ == "__main__":
    unittest.main()
