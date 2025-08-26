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

def simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if numerator % denom == 0:
        return True
    return False

def test_simplify_valid_input():
    assert simplify("2/3", "4/5") == False
    assert simplify("1/2", "3/4") == False
    assert simplify("5/7", "2/9") == False

def test_simplify_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        simplify("1/0", "2/3")
    with pytest.raises(ZeroDivisionError):
        simplify("4/5", "0/1")

def test_simplify_non_numeric_input():
    with pytest.raises(ValueError):
        simplify("a/b", "c/d")
    with pytest.raises(ValueError):
        simplify("2/3", "4/x")

@pytest.mark.parametrize("x,n,expected", [
    ("0/1", "1/1", True),
    ("1/1", "1/1", True),
    ("2/4", "1/2", True),
    ("3/6", "1/2", True),
    ("4/8", "1/2", True),
    ("5/10", "1/2", True),
    ("6/12", "1/2", True),
])
def test_simplify_positive_cases(x, n, expected):
    assert simplify(x, n) == expected