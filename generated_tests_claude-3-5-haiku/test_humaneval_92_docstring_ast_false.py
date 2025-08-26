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

def test_any_int_valid_cases():
    assert any_int(5, 2, 7) == True
    assert any_int(3, -2, 1) == True
    assert any_int(1, 2, 3) == True
    assert any_int(-1, 0, 1) == True

def test_any_int_invalid_cases():
    assert any_int(3, 2, 2) == False
    assert any_int(1, 2, 4) == False
    assert any_int(0, 0, 0) == False

def test_any_int_float_inputs():
    assert any_int(3.6, -2.2, 2) == False
    assert any_int(1.5, 2.5, 3) == False

def test_any_int_mixed_types():
    assert any_int(1, 2, '3') == False
    assert any_int('1', 2, 3) == False

@pytest.mark.parametrize("x,y,z,expected", [
    (5, 2, 7, True),
    (3, -2, 1, True),
    (1, 2, 3, True),
    (3, 2, 2, False),
    (1, 2, 4, False),
    (3.6, -2.2, 2, False),
    (1, 2, '3', False),
    (0, 0, 0, False)
])
def test_any_int_parametrized(x, y, z, expected):
    assert any_int(x, y, z) == expected