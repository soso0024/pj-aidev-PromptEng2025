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
import pytest

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (-1, 2, 1),
    (0, 0, 0),
    (10, -5, 5),
    (2147483647, 1, 2147483648),  # Maximum integer value
    (-2147483648, -1, -2147483649)  # Minimum integer value
])
def test_add(x, y, expected):
    assert add(x, y) == expected

def test_add_non_integers():
    with pytest.raises(TypeError):
        add("a", 1)
    with pytest.raises(TypeError):
        add(1, "b")
    with pytest.raises(TypeError):
        add(1.0, 2)
    with pytest.raises(TypeError):
        add(1, 2.0)

def test_add_overflow():
    with pytest.raises(OverflowError):
        add(2147483647, 1)  # Maximum integer value + 1
    with pytest.raises(OverflowError):
        add(-2147483648, -1)  # Minimum integer value - 1

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y