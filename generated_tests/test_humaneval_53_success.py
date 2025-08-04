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
    assert add(1, 2) == 3
    assert add(10, 20) == 30

def test_add_negative_numbers():
    assert add(-1, -2) == -3
    assert add(-10, -20) == -30

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 1) == 1
    assert add(1, 0) == 1

def test_add_positive_and_negative():
    assert add(-1, 1) == 0
    assert add(10, -5) == 5
    assert add(-7, 3) == -4

@pytest.mark.parametrize("x,y,expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 0, 0),
    (100, -100, 0),
    (-5, 10, 5),
    (999999, 1, 1000000)
])
def test_add_parametrized(x, y, expected):
    assert add(x, y) == expected

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
    assert add(-1000000, -2000000) == -3000000

def test_add_type_error():
    with pytest.raises(TypeError):
        add("1", 2)
    with pytest.raises(TypeError):
        add(1, "2")

def test_add_none_error():
    with pytest.raises(TypeError):
        add(None, 1)
    with pytest.raises(TypeError):
        add(1, None)
    with pytest.raises(TypeError):
        add(None, None)