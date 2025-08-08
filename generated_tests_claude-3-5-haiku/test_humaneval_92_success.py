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
    assert any_int(1, 2, 3) == True
    assert any_int(3, 1, 2) == True
    assert any_int(2, 3, 1) == True

def test_any_int_non_integer_inputs():
    assert any_int(1.5, 2, 3) == False
    assert any_int(1, 2.5, 3) == False
    assert any_int(1, 2, 3.5) == False

def test_any_int_string_inputs():
    assert any_int('1', 2, 3) == False
    assert any_int(1, '2', 3) == False
    assert any_int(1, 2, '3') == False

def test_any_int_no_sum_match():
    assert any_int(1, 2, 5) == False
    assert any_int(10, 20, 5) == False

@pytest.mark.parametrize("x,y,z,expected", [
    (0, 0, 0, True),
    (-1, 1, 0, True),
    (100, 200, 300, True),
    (-100, -200, -300, True)
])
def test_any_int_parametrized(x, y, z, expected):
    assert any_int(x, y, z) == expected

def test_any_int_mixed_signs():
    assert any_int(-1, 2, 1) == True
    assert any_int(1, -2, -1) == True
