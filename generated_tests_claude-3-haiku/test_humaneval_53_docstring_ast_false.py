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
    assert add(5, 7) == 12

def test_add_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-5, -7) == -12

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, 7) == 7

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (5, 7, 12),
    (-2, -3, -5),
    (-5, -7, -12),
    (0, 0, 0),
    (5, 0, 5),
    (0, 7, 7)
])
def test_add_with_parametrize(x, y, expected):
    assert add(x, y) == expected

def test_add_non_integers():
    with pytest.raises(TypeError):
        add(2.5, 3)
    with pytest.raises(TypeError):
        add(2, 3.5)
    with pytest.raises(TypeError):
        add('2', 3)
    with pytest.raises(TypeError):
        add(2, '3')