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
    assert simplify("1/4", "2/8") == False
    assert simplify("1/3", "2/6") == False

def test_simplify_not_equal():
    assert simplify("1/2", "1/3") == False
    assert simplify("2/3", "3/4") == False
    assert simplify("1/4", "2/3") == False

@pytest.mark.parametrize("x,n,expected", [
    ("1/1", "1/1", True),
    ("1/2", "2/1", True),
    ("2/4", "2/1", True),
    ("3/9", "3/1", True),
    ("4/8", "2/1", True),
    ("1/2", "1/3", False),
    ("2/3", "1/2", False),
    ("3/4", "2/3", False)
])
def test_simplify_parametrized(x, n, expected):
    assert simplify(x, n) == expected

def test_simplify_large_numbers():
    assert simplify("100/200", "2/1") == True
    assert simplify("1000/2000", "2/1") == True
    assert simplify("999/1000", "99/100") == False

@pytest.mark.parametrize("x,n", [
    ("1/2", "0/1"),
    ("0/0", "1/2"),
    ("1/0", "1/1")
])
def test_simplify_zero_division(x, n):
    with pytest.raises(ZeroDivisionError):
        simplify(x, n)

@pytest.mark.parametrize("x,n", [
    ("abc", "1/2"),
    ("1/2", "xyz"),
    ("1-2", "1/2"),
    ("1/", "/2"),
    ("", "1/2"),
    ("1/2", "")
])
def test_simplify_invalid_input(x, n):
    with pytest.raises((ValueError, AttributeError)):
        simplify(x, n)

def test_simplify_negative_numbers():
    assert simplify("-1/2", "-1/2") == True
    assert simplify("-1/2", "1/2") == False
    assert simplify("-2/4", "-1/2") == False

def test_simplify_mixed_signs():
    assert simplify("-1/2", "2/-4") == True
    assert simplify("1/-2", "-1/2") == True
    assert simplify("-1/-2", "1/2") == True