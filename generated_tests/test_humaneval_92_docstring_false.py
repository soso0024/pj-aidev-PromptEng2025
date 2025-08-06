# Test cases for HumanEval/92
# Generated using Claude API


def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''

    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False


# Generated test cases:
import pytest

def test_any_int_basic_true():
    assert any_int(5, 2, 7) == True
    assert any_int(3, -2, 1) == True
    assert any_int(1, 2, 3) == True

def test_any_int_basic_false():
    assert any_int(3, 2, 2) == False
    assert any_int(4, 5, 6) == False

def test_any_int_zero_values():
    assert any_int(0, 0, 0) == True
    assert any_int(0, 1, 1) == True

def test_any_int_negative_numbers():
    assert any_int(-1, -2, -3) == True
    assert any_int(-5, 3, -2) == True

def test_any_int_floating_numbers():
    assert any_int(3.0, 2.0, 1.0) == False
    assert any_int(1.5, 2.5, 4.0) == False

@pytest.mark.parametrize("x, y, z, expected", [
    (5, 2, 7, True),
    (3, 2, 2, False),
    (3, -2, 1, True),
    (3.6, -2.2, 2, False),
    (0, 0, 0, True),
    (-1, -2, -3, True),
    (10, 5, 5, True),
    (1.0, 2.0, 3.0, False),
    (100, 50, 50, True),
    (-10, -5, -15, True)
])
def test_any_int_parametrized(x, y, z, expected):
    assert any_int(x, y, z) == expected

def test_any_int_large_numbers():
    assert any_int(1000000, 2000000, 3000000) == True
    assert any_int(999999, 1, 1000000) == True

def test_any_int_mixed_types():
    assert any_int(1, 2.0, 3) == False
    assert any_int("1", 2, 3) == False
    assert any_int(1, "2", 3) == False

def test_any_int_boolean_inputs():
    assert any_int(True, False, True) == False
    assert any_int(1, True, 2) == False

def test_any_int_none_values():
    assert any_int(None, 1, 1) == False
    assert any_int(1, None, 1) == False
    assert any_int(1, 1, None) == False