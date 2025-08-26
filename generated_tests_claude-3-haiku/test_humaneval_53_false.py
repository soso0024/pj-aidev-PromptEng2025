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

def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(10, 20) == 30

def test_add_negative_numbers():
    assert add(-5, -10) == -15
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, 10) == 10

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (-1, 2, 1),
    (1, -2, -1),
    (0, 0, 0),
    (2147483647, 1, 2147483648),
    (-2147483648, -1, -2147483649)
])
def test_add_various_inputs(x, y, expected):
    assert add(x, y) == expected

def test_add_non_integers():
    with pytest.raises(TypeError):
        add(1.5, 2)
    with pytest.raises(TypeError):
        add(1, '2')
    with pytest.raises(TypeError):
        add('1', 2)