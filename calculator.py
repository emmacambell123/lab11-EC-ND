# https://github.com/emmacambell123/lab11-EC-ND/tree/main
# Partner 1: Emma Campbell
# Partner 2: Nicholas De Faria

"""
calculator.py
Defines functions used to create a simple calculator.
"""

import math


# ---- Partner 1 functions ----

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
    """Return the length of the hypotenuse."""
    return math.hypot(a, b)


# ---- Core required functions ----

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a / b


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive.")
    return math.log(b, a)


def exponentiate(a, b):
    return a ** b


# ---- Short aliases required by autograder ----
mul = multiply
div = divide
exp = exponentiate
log = logarithm
sub = subtract
