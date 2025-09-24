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
    if (numerator/denom == int(numerator/denom)):
        return True
    return False

@pytest.mark.parametrize("x,n,expected", [
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("1/1", "1/1", True),
    ("2/3", "3/2", True),
    ("1/2", "1/2", False),
    ("4/8", "2/1", True),
    ("3/7", "7/3", True),
    ("5/12", "12/5", True),
    ("1/3", "1/3", False),
    ("10/1", "1/10", True),
    ("2/4", "4/2", True),
    ("3/9", "9/3", True),
    ("1/7", "14/2", True),
    ("5/6", "6/5", True),
    ("8/9", "9/8", True),
    ("1/100", "100/1", True),
    ("7/13", "13/7", True),
    ("11/17", "17/11", True),
    ("1/4", "3/1", False),
    ("2/5", "5/3", False),
    ("3/8", "8/4", False),
    ("9/16", "16/9", True),
    ("15/25", "25/15", True),
    ("6/10", "10/6", True)
])
def test_simplify_parametrized(x, n, expected):
    assert simplify(x, n) == expected

def test_simplify_whole_numbers():
    assert simplify("5/1", "3/1") == True
    assert simplify("10/1", "7/1") == True

def test_simplify_unit_fractions():
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True

def test_simplify_reciprocals():
    assert simplify("2/3", "3/2") == True
    assert simplify("4/5", "5/4") == True
    assert simplify("7/11", "11/7") == True

def test_simplify_non_whole_results():
    assert simplify("1/3", "1/2") == False
    assert simplify("2/7", "3/5") == False
    assert simplify("4/9", "5/8") == False

def test_simplify_large_numbers():
    assert simplify("100/200", "200/100") == True
    assert simplify("999/1000", "1000/999") == True

def test_simplify_same_fractions():
    assert simplify("1/2", "1/2") == False
    assert simplify("3/4", "3/4") == False
    assert simplify("5/7", "5/7") == False

def test_simplify_equivalent_fractions():
    assert simplify("2/4", "8/4") == True
    assert simplify("3/6", "12/6") == True
    assert simplify("4/8", "16/8") == True
