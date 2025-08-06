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

@pytest.mark.parametrize("x, n, expected", [
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("1/2", "2/1", True),
    ("1/4", "4/1", True),
    ("2/3", "3/2", True),
    ("1/3", "2/1", False),
    ("10/100", "10/1", True),
    ("99/100", "100/99", True),
    ("1/1000", "1000/1", True),
    ("7/13", "13/7", True),
    ("5/6", "6/5", True),
    ("1/17", "3/2", False),
    ("123/456", "456/123", True),
    ("1/2", "1/3", False)
])
def test_simplify_parametrized(x, n, expected):
    assert simplify(x, n) == expected

def test_simplify_large_numbers():
    assert simplify("1000000/1", "1/1000000") == True
    assert simplify("999999/1000000", "1000000/999999") == True

def test_simplify_same_numbers():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/2", "2/2") == True
    assert simplify("100/100", "100/100") == True

@pytest.mark.parametrize("x, n", [
    ("1/2", "3/4"),
    ("2/5", "3/7"),
    ("7/9", "11/13"),
    ("13/17", "19/23")
])
def test_simplify_irrational_results(x, n):
    assert simplify(x, n) == False

def test_simplify_edge_cases():
    assert simplify("1/1", "1000000/1000000") == True
    assert simplify("2/4", "4/2") == True
    assert simplify("50/100", "100/50") == True

@pytest.mark.parametrize("x, n", [
    ("1/999999999", "999999999/1"),
    ("123456789/987654321", "987654321/123456789")
])
def test_simplify_very_large_numbers(x, n):
    assert simplify(x, n) == True
