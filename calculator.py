"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass
import math


def square_root(a):
    """
    Returns the square root of a.
    Raises ValueError if a < 0.
    """
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)


def hypotenuse(a, b):
    """
    Returns the hypotenuse given sides a and b.
    Negative numbers are allowed.
    """
    return math.hypot(a, b)


def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def sub(a, b):
    """Returns the difference of a and b."""
    return a - b


def mul(a, b):
    """Returns the product of a and b."""
    return a * b


def div(a, b):
    """
    Returns the result of dividing b by a.
    Raises ZeroDivisionError if a == 0.
    """
    if a == 0:
        raise ZeroDivisionError("Division by zero.")
    return b / a


def log(a, b):
    """
    Returns the logarithm of b with base a.
    Raises ValueError if a <= 0, a == 1, or b <= 0.
    """
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)


def exp(a, b):
    """Returns a raised to the power of b."""
    return a ** b


