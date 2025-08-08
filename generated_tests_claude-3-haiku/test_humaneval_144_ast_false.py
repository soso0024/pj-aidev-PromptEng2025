# Test cases for HumanEval/144
# Generated using Claude API


def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False


# Generated test cases:
import pytest
from math import gcd

def simplify(x, n):
    a, b = map(int, x.split("/"))
    c, d = map(int, n.split("/"))
    numerator = a * c
    denom = b * d
    if denom == 0:
        raise ValueError("Denominator cannot be zero")
    if numerator % denom == 0:
        return True
    return False

@pytest.mark.parametrize("x, n, expected", [
    ("3/4", "1/2", True),
    ("5/8", "1/4", True),
    ("2/3", "1/6", True),
    ("7/11", "3/5", False),
    ("0/5", "0/1", True),
    ("10/10", "2/2", True),
    ("1/2", "0/1", False),
    ("1/2", "1/0", False)
])
def test_simplify(x, n, expected):
    assert simplify(x, n) == expected

def test_invalid_input():
    with pytest.raises(ValueError):
        simplify("1/2", "0/0")
    with pytest.raises(ValueError):
        simplify("1/0", "2/3")
    with pytest.raises(ValueError):
        simplify("abc", "def")

def test_zero_denominator():
    assert not simplify("1/0", "2/3")
    assert not simplify("0/0", "2/3")

def test_zero_numerator():
    assert simplify("0/5", "0/1")
    assert not simplify("0/0", "2/3")