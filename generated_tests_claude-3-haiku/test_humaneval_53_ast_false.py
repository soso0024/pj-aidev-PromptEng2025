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

def test_add_positive_integers():
    assert add(2, 3) == 5
    assert add(10, 20) == 30

def test_add_negative_integers():
    assert add(-5, -10) == -15
    assert add(-2, 3) == 1

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, -5) == -5

@pytest.mark.parametrize("x, y, expected", [
    (1, 2.5, 3.5),
    (-3.14, 2.71, -0.43),
    (0.0, 0.0, 0.0)
])
def test_add_floats(x, y, expected):
    assert round(add(x, y), 2) == expected

def test_add_non_integers():
    with pytest.raises(TypeError):
        add('a', 'b')
    with pytest.raises(TypeError):
        add([1, 2], [3, 4])
    with pytest.raises(TypeError):
        add(None, 1)