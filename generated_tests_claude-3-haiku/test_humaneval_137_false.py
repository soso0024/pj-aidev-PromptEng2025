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

def test_compare_one_equal_floats():
    assert compare_one(1.0, 1.0) is None

def test_compare_one_equal_strings():
    assert compare_one('1.0', '1.0') is None
    assert compare_one('1.0', '1.0') is None

def test_compare_one_greater_float():
    assert compare_one(2.0, 1.0) == 2.0

def test_compare_one_greater_string():
    assert compare_one('2.0', '1.0') == '2.0'

def test_compare_one_less_float():
    assert compare_one(1.0, 2.0) == 2.0

def test_compare_one_less_string():
    assert compare_one('1.0', '2.0') == '2.0'

def test_compare_one_non_numeric_input():
    with pytest.raises(ValueError):
        compare_one('a', '1.0')
    with pytest.raises(ValueError):
        compare_one(1.0, 'a')

@pytest.mark.parametrize("a,b,expected", [
    ('1.0', '1.0', None),
    (1.0, 1.0, None),
    ('2.0', '1.0', '2.0'),
    (2.0, 1.0, 2.0),
    ('1.0', '2.0', '2.0'),
    (1.0, 2.0, 2.0),
    ('a', '1.0', pytest.raises(ValueError)),
    (1.0, 'a', pytest.raises(ValueError))
])
def test_compare_one_parametrized(a, b, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            compare_one(a, b)
    else:
        assert compare_one(a, b) == expected