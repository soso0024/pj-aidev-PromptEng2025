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

def test_simplify():
    assert simplify("1/2", "2/4") == True
    assert simplify("1/2", "3/6") == False
    assert simplify("2/4", "1/2") == True
    assert simplify("3/6", "1/2") == True
    assert simplify("4/8", "1/2") == True
    assert simplify("5/10", "1/2") == True
    assert simplify("1/3", "2/6") == False