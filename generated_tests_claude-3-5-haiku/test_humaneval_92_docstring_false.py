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

def any_int(x, y, z):
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False

def test_any_int_basic_cases():
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True

def test_any_int_sum_conditions():
    assert any_int(1, 2, 3) == True
    assert any_int(2, 1, 3) == True
    assert any_int(3, 1, 2) == True

def test_any_int_non_integer_inputs():
    assert any_int(3.6, -2.2, 2) == False
    assert any_int(1.5, 2, 3) == False
    assert any_int(1, 2.5, 3) == False

def test_any_int_zero_cases():
    assert any_int(0, 0, 0) == False
    assert any_int(1, -1, 0) == True
    assert any_int(0, 1, 1) == True

def test_any_int_negative_numbers():
    assert any_int(-1, -2, -3) == True
    assert any_int(-5, 2, -3) == True
    assert any_int(-1, -1, -2) == True

@pytest.mark.parametrize("x,y,z,expected", [
    (5, 2, 7, True),
    (3, 2, 2, False),
    (3, -2, 1, True),
    (1, 2, 3, True),
    (3.6, -2.2, 2, False),
    (0, 0, 0, False),
    (-1, -2, -3, True)
])
def test_any_int_parametrized(x, y, z, expected):
    assert any_int(x, y, z) == expected