# Test cases for HumanEval/137
# Generated using Claude API


def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """

    temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): return None
    return a if float(temp_a) > float(temp_b) else b 


# Generated test cases:
import pytest
from math import isclose

def compare_one(a, b):
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    if a is None or b is None:
        return None
    if float(temp_a) == float(temp_b): return None
    return a if float(temp_a) > float(temp_b) else b

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, None),
    (2.0, 1.5, 2.0),
    (1.5, 2.0, 1.5),
    ("1.2", "1.2", None),
    ("2.5", "1.8", "2.5"),
    ("1.8", "2.5", "1.8"),
    ("1,2", "1.2", 1.2),
    ("2,5", "1.8", 2.5),
    ("1,8", "2.5", 1.8),
    (None, 1.0, 1.0),
    (1.0, None, 1.0),
    (None, None, None),
])
def test_compare_one(a, b, expected):
    result = compare_one(a, b)
    if expected is None:
        assert result is None
    else:
        assert isclose(float(result), float(expected))