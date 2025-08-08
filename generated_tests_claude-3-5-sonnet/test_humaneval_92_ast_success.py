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
    assert any_int(5, 3, 8) == True
    assert any_int(8, 5, 3) == True
    assert any_int(3, 8, 5) == True

def test_any_int_basic_false():
    assert any_int(1, 2, 4) == False
    assert any_int(5, 2, 2) == False

def test_any_int_zero():
    assert any_int(0, 0, 0) == True
    assert any_int(0, 5, 5) == True

def test_any_int_negative():
    assert any_int(-2, 5, 3) == True
    assert any_int(-5, -3, -8) == True

@pytest.mark.parametrize("x,y,z,expected", [
    (1.0, 2, 3, False),
    (1, 2.0, 3, False),
    (1, 2, 3.0, False),
    ("1", 2, 3, False),
    (None, 2, 3, False),
    ([], 2, 3, False),
    ({}, 2, 3, False)
])
def test_any_int_invalid_types(x, y, z, expected):
    assert any_int(x, y, z) == expected

def test_any_int_large_numbers():
    assert any_int(1000000, 2000000, 3000000) == True
    assert any_int(1000000, 2000000, 4000000) == False

def test_any_int_same_numbers():
    assert any_int(5, 5, 10) == True
    assert any_int(5, 10, 5) == True
    assert any_int(10, 5, 5) == True

def test_any_int_min_max():
    assert any_int(-2147483648, 2147483647, -1) == True
    assert any_int(2147483647, -2147483648, -1) == True

@pytest.mark.parametrize("x,y,z,expected", [
    (0, 0, 0, True),
    (1, 1, 2, True),
    (-1, -1, -2, True),
    (10, -5, 5, True),
    (100, 50, 150, True),
    (1, 2, 5, False),
    (0, 1, 3, False),
    (-1, -2, -5, False)
])
def test_any_int_parametrized(x, y, z, expected):
    assert any_int(x, y, z) == expected