# https://github.com/emmacambell123/lab11-EC-ND/tree/main
# Partner 1: Emma Campbell
# Partner 2: Nicholas De Faria

"""
calculator.py
Defines functions used to create a simple calculator.

"""

import math


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def mul(a, b):
    """Return a * b."""
    return a * b


def div(a, b):
    """
    Return a / b.

    Raises:
        ZeroDivisionError: if b == 0.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a / b


def logarithm(a, b):
    """
    Return log_a(b) using math.log(b, a).

    Raises:
        ValueError: if
            - base a <= 0
            - base a == 1
            - argument b <= 0
    """
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive.")
    return math.log(b, a)


def exp(a, b):
    """Return a ** b."""
    return a ** b


def square_root(a):
    """
    Return the square root of a.

    Raises:
        ValueError: if a < 0.
    """
    if a < 0:
        raise ValueError("square_root is undefined for negative numbers.")
    return math.sqrt(a)


def hypotenuse(a, b):
    """
    Return the length of the hypotenuse given legs a and b.
    """
    return math.hypot(a, b)
