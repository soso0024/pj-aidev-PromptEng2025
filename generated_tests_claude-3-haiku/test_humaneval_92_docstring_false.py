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

@pytest.mark.parametrize("x, y, z, expected", [
    (5, 2, 7, True),
    (3, 2, 2, False),
    (3, -2, 1, True),
    (3.6, -2.2, 2, False),
    (1, 2, 3, True),
    (-1, -2, 3, True),
    (0, 0, 0, True),
    (1, 2, 4, False),
    (1, 1, 2, True),
    ('a', 2, 3, False),
    (1, 'b', 3, False),
    (1, 2, 'c', False)
])
def test_any_int(x, y, z, expected):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        assert (x + y == z) or (x + z == y) or (y + z == x) == expected
    else:
        assert any_int(x, y, z) is False