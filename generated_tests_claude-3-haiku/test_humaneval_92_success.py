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

def test_any_int_valid_inputs():
    assert any_int(1, 2, 3) is True
    assert any_int(4, 5, 9) is True
    assert any_int(7, 2, 5) is True

def test_any_int_invalid_inputs():
    assert any_int(1.0, 2, 3) is False
    assert any_int(1, 2.0, 3) is False
    assert any_int(1, 2, 3.0) is False
    assert any_int('a', 2, 3) is False
    assert any_int(1, 'b', 3) is False
    assert any_int(1, 2, 'c') is False

@pytest.mark.parametrize("x, y, z", [
    (1, 2, 3),
    (4, 5, 9),
    (7, 2, 5),
    (1.0, 2, 3),
    (1, 2.0, 3),
    (1, 2, 3.0),
    ('a', 2, 3),
    (1, 'b', 3),
    (1, 2, 'c')
])
def test_any_int_with_parametrize(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if (x + y == z) or (x + z == y) or (y + z == x):
            assert any_int(x, y, z) is True
        else:
            assert any_int(x, y, z) is False
    else:
        assert any_int(x, y, z) is False

def test_any_int_edge_cases():
    assert any_int(0, 0, 0) is True
    assert any_int(-1, -1, -2) is True
    assert any_int(-1, 0, 1) is True
    assert any_int(0, 0, 1) is False
    assert any_int(0, 1, 0) is False
    assert any_int(1, 0, 0) is False
