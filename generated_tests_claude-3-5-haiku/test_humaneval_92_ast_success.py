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

def test_any_int_valid_combinations():
    assert any_int(5, 2, 7) == True
    assert any_int(3, 4, 7) == True
    assert any_int(1, 2, 3) == True

def test_any_int_invalid_combinations():
    assert any_int(5, 2, 8) == False
    assert any_int(3, 4, 6) == False

def test_any_int_non_integer_inputs():
    assert any_int(5.5, 2, 7) == False
    assert any_int(5, '2', 7) == False
    assert any_int(5, 2, '7') == False

def test_any_int_zero_inputs():
    assert any_int(0, 0, 0) == True
    assert any_int(5, 0, 5) == True
    assert any_int(0, 5, 5) == True

def test_any_int_negative_inputs():
    assert any_int(-5, 2, -3) == True
    assert any_int(-1, -2, -3) == True
    assert any_int(5, -2, 3) == True

@pytest.mark.parametrize("x,y,z,expected", [
    (5, 2, 7, True),
    (3, 4, 7, True),
    (1, 2, 3, True),
    (5, 2, 8, False),
    (3, 4, 6, False),
    (0, 0, 0, True),
    (-5, 2, -3, True),
    (5.5, 2, 7, False),
    (5, '2', 7, False)
])
def test_any_int_parametrized(x, y, z, expected):
    assert any_int(x, y, z) == expected
