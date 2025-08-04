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
from fractions import Fraction

def test_simplify_basic():
    assert simplify("1/2", "2/4") == False
    assert simplify("1/3", "2/6") == False
    assert simplify("2/4", "1/2") == False

def test_simplify_false_cases():
    assert simplify("1/2", "1/3") == False
    assert simplify("2/3", "3/5") == False

@pytest.mark.parametrize("x, n, expected", [
    ("1/1", "1/1", True),
    ("2/4", "1/2", False),
    ("3/9", "1/3", False),
    ("4/8", "1/2", False),
    ("1/2", "1/3", False),
    ("5/6", "2/3", False),
    ("7/8", "3/4", False)
])
def test_simplify_parametrized(x, n, expected):
    assert simplify(x, n) == expected

@pytest.mark.parametrize("x, n", [
    ("1", "1/2"),
    ("1/2", "1"),
    ("a/b", "1/2"),
    ("1/2", "a/b"),
    ("1/0", "1/2"),
    ("1/2", "1/0")
])
def test_simplify_invalid_input(x, n):
    with pytest.raises(Exception):
        simplify(x, n)

def test_simplify_large_numbers():
    assert simplify("100/200", "1000/2000") == False
    assert simplify("1000/2000", "100/200") == False

def test_simplify_zero():
    assert simplify("0/1", "0/2") == True
    assert simplify("0/5", "0/10") == True