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
from your_module import any_int
import pytest

@pytest.mark.parametrize("x, y, z", [
    (1, 2, 3), (2, 1, 3), (3, 2, 1), (1, 1, 2), (2, 2, 4), (3, 3, 6),
    (0, 0, 0), (-1, 1, 0), (1, -1, 0), (0, 1, -1), (1, 0, -1), (-1, 0, 1),
    (1, 2, 3), (1, 2, 3), (1, 2, 3), (2, 3, 1), (3, 1, 2), (2, 1, 3)
])
def test_any_int(x, y, z):
    if (x + y == z) or (x + z == y) or (y + z == x):
        assert any_int(x, y, z) is True
    else:
        assert any_int(x, y, z) is False