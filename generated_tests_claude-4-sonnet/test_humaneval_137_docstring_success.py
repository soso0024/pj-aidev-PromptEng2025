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

def compare_one(a, b):
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): return None
    return a if float(temp_a) > float(temp_b) else b 

def test_compare_one_int_float():
    assert compare_one(1, 2.5) == 2.5
    assert compare_one(5, 3.2) == 5
    assert compare_one(0, 1.0) == 1.0
    assert compare_one(-1, 0.5) == 0.5
    assert compare_one(10, -5.5) == 10

def test_compare_one_string_comma():
    assert compare_one(1, "2,3") == "2,3"
    assert compare_one("5,1", "6") == "6"
    assert compare_one("3,7", 2) == "3,7"
    assert compare_one("1,5", "2,8") == "2,8"
    assert compare_one("10,0", "9,9") == "10,0"

def test_compare_one_string_dot():
    assert compare_one("1.5", 2) == 2
    assert compare_one("3.7", "2.1") == "3.7"
    assert compare_one(1, "2.5") == "2.5"
    assert compare_one("5.0", 4.9) == "5.0"

def test_compare_one_equal_values():
    assert compare_one("1", 1) is None
    assert compare_one(2, 2.0) is None
    assert compare_one("3,0", 3) is None
    assert compare_one("4.5", "4,5") is None
    assert compare_one(0, "0,0") is None
    assert compare_one("7", "7.0") is None

def test_compare_one_negative_numbers():
    assert compare_one(-1, -2) == -1
    assert compare_one("-3,5", -2) == -2
    assert compare_one("-1.5", "-2,7") == "-1.5"
    assert compare_one(-5, "-4,9") == "-4,9"

def test_compare_one_zero_values():
    assert compare_one(0, "0") is None
    assert compare_one("0,0", 0.0) is None
    assert compare_one(0, 1) == 1
    assert compare_one("0", -1) == "0"

def test_compare_one_large_numbers():
    assert compare_one(1000000, "999999,9") == 1000000
    assert compare_one("1000000,1", 1000000) == "1000000,1"

def test_compare_one_small_decimals():
    assert compare_one("0,001", "0.002") == "0.002"
    assert compare_one(0.0001, "0,0002") == "0,0002"

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 2),
    (3.5, 2.1, 3.5),
    ("4,5", 3, "4,5"),
    ("2.7", "3,1", "3,1"),
    (5, 5, None),
    ("6", 6.0, None),
    (-1, -2, -1),
    ("0", 0, None)
])
def test_compare_one_parametrized(a, b, expected):
    assert compare_one(a, b) == expected
