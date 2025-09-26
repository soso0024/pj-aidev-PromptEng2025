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
    assert any_int(3.6, -2.2, 2) == False

def test_any_int_all_permutations():
    assert any_int(1, 2, 3) == True  # 1 + 2 = 3
    assert any_int(2, 1, 3) == True  # 2 + 1 = 3
    assert any_int(3, 1, 2) == True  # 1 + 2 = 3
    assert any_int(1, 3, 2) == True  # 1 + 2 = 3
    assert any_int(2, 3, 1) == True  # 2 + 1 = 3
    assert any_int(3, 2, 1) == True  # 2 + 1 = 3

def test_any_int_negative_numbers():
    assert any_int(-1, -2, -3) == True  # -1 + (-2) = -3
    assert any_int(-5, 3, -2) == True   # -5 + 3 = -2
    assert any_int(10, -5, 5) == True   # -5 + 5 = 0, 10 + (-5) = 5
    assert any_int(-1, -1, -2) == True  # -1 + (-1) = -2

def test_any_int_zeros():
    assert any_int(0, 0, 0) == True     # 0 + 0 = 0
    assert any_int(0, 5, 5) == True     # 0 + 5 = 5
    assert any_int(5, 0, 5) == True     # 5 + 0 = 5
    assert any_int(5, 5, 0) == True     # 5 + 0 = 5
    assert any_int(0, 1, 2) == False    # no sum equals

def test_any_int_no_valid_sum():
    assert any_int(1, 2, 4) == False
    assert any_int(1, 1, 1) == False
    assert any_int(10, 20, 40) == False
    assert any_int(-1, -2, -4) == False

def test_any_int_float_inputs():
    assert any_int(1.0, 2, 3) == False
    assert any_int(1, 2.0, 3) == False
    assert any_int(1, 2, 3.0) == False
    assert any_int(1.5, 2.5, 4.0) == False
    assert any_int(1.1, 2.2, 3.3) == False

def test_any_int_string_inputs():
    assert any_int("1", 2, 3) == False
    assert any_int(1, "2", 3) == False
    assert any_int(1, 2, "3") == False
    assert any_int("1", "2", "3") == False

def test_any_int_none_inputs():
    assert any_int(None, 2, 3) == False
    assert any_int(1, None, 3) == False
    assert any_int(1, 2, None) == False
    assert any_int(None, None, None) == False

def test_any_int_boolean_inputs():
    assert any_int(True, 2, 3) == True   # True is instance of int in Python, True == 1
    assert any_int(False, 1, 1) == True  # False == 0, so 0 + 1 = 1
    assert any_int(True, True, False) == True  # 1 + 1 = 2, but True + False = 1, so 1 + 0 = 1

def test_any_int_large_numbers():
    assert any_int(1000000, 2000000, 3000000) == True
    assert any_int(-1000000, -2000000, -3000000) == True
    assert any_int(1000000, 2000000, 4000000) == False

@pytest.mark.parametrize("x,y,z,expected", [
    (1, 2, 3, True),
    (1, 2, 4, False),
    (0, 0, 0, True),
    (-1, 1, 0, True),
    (1.0, 2, 3, False),
    ("1", 2, 3, False),
    (None, 2, 3, False)
])
def test_any_int_parametrized(x, y, z, expected):
    assert any_int(x, y, z) == expected