# https://github.com/emmacambell123/lab11-EC-ND/tree/main
# Partner 1: Emma Campbell
# Partner 2: Nicholas De Faria

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    """
    Unit tests for calculator.py

    Partner 2 responsibilities:
        - test_add
        - test_subtract
        - test_divide_by_zero
        - test_logarithm
        - test_log_invalid_base
    """

    ######### Partner 2 Tests #########

    def test_add(self):
        """Test the add function with several cases."""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """Test the subtract function with several cases."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)
        self.assertEqual(subtract(-2, -2), 0)

    def test_divide_by_zero(self):
        """divide should raise ZeroDivisionError when dividing by zero."""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_logarithm(self):
        """Test the logarithm function with valid inputs."""
        # log_10(1000) = 3
        self.assertAlmostEqual(logarithm(10, 1000), 3.0)

        # log_2(8) = 3
        self.assertAlmostEqual(logarithm(2, 8), 3.0)

        # log_5(25) = 2
        self.assertAlmostEqual(logarithm(5, 25), 2.0)

    def test_log_invalid_base(self):
        """
        logarithm should raise ValueError for invalid bases:
        - base <= 0
        - base == 1
        """
        with self.assertRaises(ValueError):
            logarithm(0, 10)

        with self.assertRaises(ValueError):
            logarithm(-2, 10)

        with self.assertRaises(ValueError):
            logarithm(1, 10)

    ######### Partner 1 Tests (Emma’s section) #########

    # def test_multiply(self):
    #     """Partner 1: test multiply function."""
    #     pass
    #
    # def test_divide(self):
    #     """Partner 1: test divide function with normal cases."""
    #     pass
    #
    # def test_log_invalid_argument(self):
    #     """Partner 1: logarithm should raise ValueError for invalid arguments (b <= 0)."""
    #     pass
    #
    # def test_hypotenuse(self):
    #     """Partner 1: test hypotenuse function."""
    #     pass
    #
    # def test_sqrt(self):
    #     """Partner 1: test square_root function (including negative input)."""
    #     pass


if __name__ == "__main__":
    unittest.main()
