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

    Partner 1 will complete the remaining tests.
    """

    ######### Partner 2 Tests #########

    def test_add(self):
        """Test the add function with several cases."""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """Test the sub function with several cases."""
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 4), -4)
        self.assertEqual(sub(-2, -2), 0)

    def test_divide_by_zero(self):
        """div should raise ZeroDivisionError when dividing by zero."""
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_logarithm(self):
        """Test the log function with valid inputs."""
        # log_10(1000) = 3
        self.assertAlmostEqual(log(10, 1000), 3.0)

        # log_2(8) = 3
        self.assertAlmostEqual(log(2, 8), 3.0)

        # log_5(25) = 2
        self.assertAlmostEqual(log(5, 25), 2.0)

    def test_log_invalid_base(self):
        """
        log should raise ValueError for invalid bases:
        - base <= 0
        - base == 1
        """
        with self.assertRaises(ValueError):
            log(0, 10)

        with self.assertRaises(ValueError):
            log(-2, 10)

        with self.assertRaises(ValueError):
            log(1, 10)

    ######### Partner 1 Tests (to be completed by Emma) #########

    # def test_multiply(self):
    #     """Partner 1: test mul function."""
    #     pass
    #
    # def test_divide(self):
    #     """Partner 1: test div function with normal cases."""
    #     pass
    #
    # def test_log_invalid_argument(self):
    #     """Partner 1: log should raise ValueError for invalid arguments (b <= 0)."""
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
