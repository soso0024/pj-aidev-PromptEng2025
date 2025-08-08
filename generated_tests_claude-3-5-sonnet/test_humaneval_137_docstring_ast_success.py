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

@pytest.mark.parametrize("a, b, expected", [
    (1, 2.5, 2.5),
    (2.5, 1, 2.5),
    ("2,3", 1, "2,3"),
    (1, "2,3", "2,3"),
    ("5,1", "6", "6"),
    ("6", "5,1", "6"),
    (1, 1, None),
    ("1", 1, None),
    (1, "1", None),
    ("1,0", "1.0", None),
    (1.5, 1.5, None),
    ("1,5", "1.5", None),
    (10, 2, 10),
    (-1, -2, -1),
    ("0,5", "0.5", None),
    ("10,5", 10.5, None),
    (10.5, "10,5", None),
])
def test_compare_one_parametrized(a, b, expected):
    assert compare_one(a, b) == expected

def test_compare_one_invalid_input():
    with pytest.raises(ValueError):
        compare_one("abc", 1)
    
    with pytest.raises(ValueError):
        compare_one(1, "def")
        
    with pytest.raises(ValueError):
        compare_one("abc", "def")

def test_compare_one_none_input():
    with pytest.raises(TypeError):
        compare_one(None, 1)
    
    with pytest.raises(TypeError):
        compare_one(1, None)
        
    with pytest.raises(TypeError):
        compare_one(None, None)

def test_compare_one_empty_string():
    with pytest.raises(ValueError):
        compare_one("", 1)
    
    with pytest.raises(ValueError):
        compare_one(1, "")
        
    with pytest.raises(ValueError):
        compare_one("", "")