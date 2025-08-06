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

@pytest.mark.parametrize("x,n,expected", [
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("1/1", "1/1", True),
    ("2/3", "3/2", True),
    ("1/4", "2/3", False),
    ("5/6", "6/5", True),
    ("10/20", "20/10", True),
    ("1/100", "50/1", False),
    ("99/100", "100/99", True)
])
def test_simplify_basic_cases(x, n, expected):
    assert simplify(x, n) == expected

@pytest.mark.parametrize("x,n,expected", [
    ("1/1000000", "1000000/1", True),
    ("1/999999", "999999/1", True),
    ("2/1000000", "500000/1", True),
    ("1/1000000", "999999/1", False)
])
def test_simplify_large_numbers(x, n, expected):
    assert simplify(x, n) == expected

@pytest.mark.parametrize("x,n,expected", [
    ("1/2", "2/4", False),
    ("3/6", "6/3", True),
    ("10/20", "20/10", True),
    ("15/30", "30/15", True)
])
def test_simplify_reducible_fractions(x, n, expected):
    assert simplify(x, n) == expected

def validate_fraction(frac):
    try:
        num, den = frac.split('/')
        num, den = int(num), int(den)
        if den <= 0 or num < 0:
            return False
        return True
    except:
        return False

@pytest.mark.parametrize("x,n", [
    ("1", "1/2"),
    ("1/2/3", "1/2"),
    ("a/b", "1/2"),
    ("1/2", "c/d"),
    ("1/-2", "1/2"),
    ("1/2", "1/-2"),
    ("0/1", "1/2")
])
def test_simplify_invalid_input(x, n):
    if not validate_fraction(x) or not validate_fraction(n):
        try:
            simplify(x, n)
            pytest.fail("Expected ValueError")
        except (ValueError, ZeroDivisionError):
            pass

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/2", "3/3") == True
    assert simplify("1/2", "1/3") == False