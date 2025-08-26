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
import math

def simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    
    if denom == 0 or int(c) == 0:
        return False
    
    gcd = math.gcd(numerator, denom)
    reduced_numerator = numerator // gcd
    reduced_denom = denom // gcd
    
    return reduced_numerator / reduced_denom == int(reduced_numerator / reduced_denom)

def test_simplify_basic_cases():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False

@pytest.mark.parametrize("x,n,expected", [
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("2/3", "3/2", True),
    ("4/6", "2/3", True),
    ("1/2", "2/4", True),
    ("5/1", "1/5", True),
    ("3/4", "4/3", False)
])
def test_simplify_parametrized(x, n, expected):
    assert simplify(x, n) == expected

def test_simplify_whole_number_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/1", "1/2") == True
    assert simplify("10/2", "5/1") == True

def test_simplify_zero_cases():
    assert simplify("0/1", "1/1") == True
    assert simplify("1/1", "0/1") == False