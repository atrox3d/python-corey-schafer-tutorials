###################################################################################################
#   https://youtu.be/6tNS--WetLI
###################################################################################################
"""
this is the module being tested
"""


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('cannot divide by 0')
    return x / y
