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
    return abs(numerator) % abs(denom) == 0

def test_simplify_basic_case():
    assert simplify("1/2", "2/4") == True

def test_simplify_non_reducible():
    assert simplify("1/3", "2/5") == False

def test_simplify_whole_number_result():
    assert simplify("2/4", "1/2") == True

def test_simplify_negative_fractions():
    assert simplify("-1/2", "-2/4") == True

def test_simplify_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        simplify("1/0", "2/3")

@pytest.mark.parametrize("x,n,expected", [
    ("1/2", "2/4", True),
    ("3/4", "6/8", True),
    ("1/3", "2/5", False),
    ("-2/4", "-1/2", True),
    ("5/10", "1/2", True)
])
def test_simplify_parametrized(x, n, expected):
    assert simplify(x, n) == expected

def test_simplify_large_numbers():
    assert simplify("1000/2000", "1/2") == True

def test_simplify_invalid_input():
    with pytest.raises(ValueError):
        simplify("invalid", "2/3")