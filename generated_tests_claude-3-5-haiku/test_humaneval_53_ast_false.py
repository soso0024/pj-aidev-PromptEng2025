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

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_mixed_signs():
    assert add(-2, 3) == 1

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

@pytest.mark.parametrize("x,y,expected", [
    (2, 3, 5),
    (-2, -3, -5),
    (-2, 3, 1),
    (0, 5, 5),
    (1000000, 2000000, 3000000)
])
def test_add_parametrized(x, y, expected):
    assert add(x, y) == expected

def test_add_type_error():
    with pytest.raises(TypeError):
        add("2", 3)
    with pytest.raises(TypeError):
        add(2, "3")

def test_add_float_error():
    with pytest.raises(TypeError):
        add(2.5, 3)
    with pytest.raises(TypeError):
        add(2, 3.5)