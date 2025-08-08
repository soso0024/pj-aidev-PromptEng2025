# Test cases for HumanEval/53
# Generated using Claude API



def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """

    return x + y


# Generated test cases:
from add import add
import pytest

@pytest.mark.parametrize("x, y, expected", [
    (0, 0, 0),
    (1, 1, 2),
    (-1, 1, 0),
    (2, 3, 5),
    (-2, -3, -5),
    (2147483647, 1, 2147483648),
    (-2147483648, -1, -2147483649)
])
def test_add(x, y, expected):
    assert add(x, y) == expected

def test_add_non_integers():
    with pytest.raises(TypeError):
        add("a", "b")
    with pytest.raises(TypeError):
        add(1.0, 2.0)