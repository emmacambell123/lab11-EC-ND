# https://github.com/emmacambell123/lab11-EC-ND/tree/main
# Partner 1: Emma Campbell
# Partner 2: Nicholas De Faria

"""
calculator.py
Defines functions used to create a simple calculator.
"""

import math


# ---- Functions originally from Partner 1 ----

def square_root(a):
    """
    Return the square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("square_root is undefined for negative numbers.")
    return math.sqrt(a)


def hypotenuse(a, b):
    """
    Return the length of the hypotenuse given legs a and b.
    """
    return math.hypot(a, b)


# ---- Functions implemented by Partner 2 ----

def add(a, b):
    """
    Return the sum of a and b.
    """
    return a + b


def sub(a, b):
    """
    Return the result of a - b.
    """
    return a - b


def mul(a, b):
    """
    Return the product of a and b.
    """
    return a * b


def div(a, b):
    """
    Return the result of a / b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a / b


def log(a, b):
    """
    Return the logarithm of b with base a, i.e. log_a(b).

    Uses math.log(b, a).

    Raises:
        ValueError: If base a <= 0, a == 1, or argument b <= 0.
    """
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive.")
    return math.log(b, a)


def exp(a, b):
    """
    Return a raised to the power of b (a ** b).
    """
    return a ** b
