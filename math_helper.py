# math_helper.py
import math

def power(base, exp):
    return base ** exp

def sqrt(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(number)
