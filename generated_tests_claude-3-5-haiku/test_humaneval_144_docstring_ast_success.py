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

def test_simplify_whole_number_result():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("4/2", "2/4") == True

def test_simplify_non_whole_number_result():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("3/4", "5/6") == False

@pytest.mark.parametrize("x,n,expected", [
    ("1/5", "5/1", True),
    ("2/3", "3/2", True),
    ("4/2", "2/4", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("3/4", "5/6", False),
    ("10/2", "5/1", True),
    ("15/3", "2/1", True)
])
def test_simplify_parametrized(x, n, expected):
    assert simplify(x, n) == expected

def test_simplify_large_numbers():
    assert simplify("100/25", "4/1") == True
    assert simplify("1000/500", "2/1") == True

def test_simplify_same_fraction():
    assert simplify("1/1", "1/1") == True
