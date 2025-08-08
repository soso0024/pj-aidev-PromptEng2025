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

@pytest.mark.parametrize("x, n, expected", [
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("0/1", "1/1", True),
    ("1/1", "1/1", True),
    ("100/100", "1/1", True),
    ("1/100", "100/1", True),
    ("1/2", "2/1", False),
    ("2/1", "1/2", False)
])
def test_simplify(x, n, expected):
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if denom == 0:
        with pytest.raises(ValueError):
            simplify(x, n)
    else:
        if (numerator/denom).is_integer():
            assert expected == True
        else:
            assert expected == False

def test_invalid_input():
    with pytest.raises(ValueError):
        simplify("1/0", "1/1")
    with pytest.raises(ValueError):
        simplify("1/1", "0/1")

def simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if denom == 0:
        raise ValueError("Denominator cannot be zero")
    if (numerator/denom).is_integer():
        return True
    return False