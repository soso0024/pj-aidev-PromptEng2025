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

def test_compare_one_numeric_inputs():
    assert compare_one(1, 2.5) == 2.5
    assert compare_one(5, 3) == 5
    assert compare_one(-1, -2) == -1

def test_compare_one_string_inputs():
    assert compare_one("1,5", "2.3") == "2.3"
    assert compare_one("5,1", "6") == "6"
    assert compare_one("10,5", "10.5") == "10.5"

def test_compare_one_mixed_inputs():
    assert compare_one(1, "2,5") == "2,5"
    assert compare_one("1", 2) == 2
    assert compare_one(1.5, "1,5") == 1.5

def test_compare_one_equal_inputs():
    assert compare_one(1, 1) is None
    assert compare_one("1", 1) is None
    assert compare_one("1,5", 1.5) is None

def test_compare_one_edge_cases():
    assert compare_one(0, 0.0) is None
    assert compare_one("0,0", 0) is None
    assert compare_one(float('inf'), 100) == float('inf')

def test_compare_one_decimal_inputs():
    assert compare_one(1.1, 1.2) == 1.2
    assert compare_one("1,1", "1.2") == "1.2"

@pytest.mark.parametrize("a,b,expected", [
    (1, 2.5, 2.5),
    ("1,5", "2.3", "2.3"),
    (1, "2,5", "2,5"),
    (1.5, "1,5", 1.5),
    (1, 1, None),
    ("1", 1, None)
])
def test_compare_one_parametrized(a, b, expected):
    assert compare_one(a, b) == expected