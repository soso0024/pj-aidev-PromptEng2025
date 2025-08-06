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
    assert any_int(10, 5, 5) == True

def test_any_int_basic_false():
    assert any_int(3, 2, 2) == False
    assert any_int(4, 5, 6) == False

def test_any_int_zero_and_negative():
    assert any_int(0, 0, 0) == True
    assert any_int(-5, -3, -8) == True
    assert any_int(-2, 5, 3) == True

def test_any_int_non_integers():
    assert any_int(3.6, -2.2, 2) == False
    assert any_int(1.0, 2, 3) == False
    assert any_int(5, 2.5, 7.5) == False

@pytest.mark.parametrize("x, y, z, expected", [
    (5, 2, 7, True),
    (3, 2, 2, False),
    (3, -2, 1, True),
    (3.6, -2.2, 2, False),
    (0, 0, 0, True),
    (-5, -3, -8, True),
    (10, 5, 5, True),
    (4, 5, 6, False),
    (1.0, 2, 3, False),
    (-2, 5, 3, True)
])
def test_any_int_parametrized(x, y, z, expected):
    assert any_int(x, y, z) == expected

@pytest.mark.parametrize("x, y, z", [
    ("string", 2, 3),
    (1, "string", 3),
    (1, 2, "string"),
    (None, None, None),
    ([], {}, ()),
    (True, False, True)
])
def test_any_int_invalid_inputs(x, y, z):
    try:
        result = any_int(x, y, z)
        assert result == False
    except:
        assert True

def test_any_int_large_numbers():
    assert any_int(1000000, 2000000, 3000000) == True
    assert any_int(-1000000, -2000000, -3000000) == True

def test_any_int_edge_cases():
    assert any_int(0, 0, 0) == True
    assert any_int(-1, -1, -2) == True
    assert any_int(2147483647, -2147483648, -1) == True