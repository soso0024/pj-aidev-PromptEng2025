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
    assert add(5, 7) == 12

def test_add_negative_integers():
    assert add(-2, -3) == -5
    assert add(-5, -7) == -12

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, 7) == 7

def test_add_large_integers():
    assert add(2**31 - 1, 1) == 2**31
    assert add(-2**31, 1) == -2**31 + 1

def test_add_float_and_int():
    with pytest.raises(TypeError):
        add(2.5, 3)
    with pytest.raises(TypeError):
        add(2, 3.5)

def test_add_non_numeric_types():
    with pytest.raises(TypeError):
        add('2', '3')
    with pytest.raises(TypeError):
        add([2], [3])
    with pytest.raises(TypeError):
        add(None, 3)
    with pytest.raises(TypeError):
        add(3, None)