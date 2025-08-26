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

def test_simplify_basic_simplifiable():
    assert simplify("1/2", "2/1") == True

def test_simplify_basic_not_simplifiable():
    assert simplify("1/3", "2/1") == False

def test_simplify_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        simplify("1/0", "2/1")

def test_simplify_negative_fractions():
    assert simplify("-1/2", "2/-1") == True

def test_simplify_large_numbers():
    assert simplify("100/50", "2/1") == True

def test_simplify_non_integer_input():
    with pytest.raises(ValueError):
        simplify("1.5/2", "3/1")

@pytest.mark.parametrize("x,n,expected", [
    ("1/2", "2/1", True),
    ("3/4", "4/3", True),
    ("5/6", "7/8", False),
    ("10/5", "2/1", True),
    ("-2/4", "1/-2", True)
])
def test_simplify_parametrized(x, n, expected):
    assert simplify(x, n) == expected