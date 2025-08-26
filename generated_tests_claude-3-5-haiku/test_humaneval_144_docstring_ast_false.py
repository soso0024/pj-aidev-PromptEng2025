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
    return numerator % denom == 0 and numerator / denom == int(numerator / denom)

def test_simplify_whole_number_result():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("4/6", "3/4") == False

def test_simplify_non_whole_number_result():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/5") == False

@pytest.mark.parametrize("x,n,expected", [
    ("1/1", "1/1", True),
    ("10/2", "5/1", True),
    ("3/4", "4/3", False),
    ("7/8", "8/7", False),
    ("12/3", "4/1", True)
])
def test_simplify_parametrized(x, n, expected):
    assert simplify(x, n) == expected

def test_simplify_large_numbers():
    assert simplify("100/10", "10/1") == True
    assert simplify("999/333", "333/999") == True

def test_simplify_prime_fractions():
    assert simplify("2/3", "3/2") == True
    assert simplify("5/7", "7/5") == False