# Test cases for HumanEval/97
# Generated using Claude API


def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """

    return abs(a % 10) * abs(b % 10)


# Generated test cases:
import pytest

def multiply(a, b):
    return abs(int(a) % 10) * abs(int(b) % 10)

def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12
    assert multiply(7, 8) == 56
    assert multiply(12, 15) == 0

def test_multiply_negative_numbers():
    assert multiply(-3, -4) == 12
    assert multiply(-7, -8) == 56
    assert multiply(-12, -15) == 0

def test_multiply_zero():
    assert multiply(0, 0) == 0
    assert multiply(0, 5) == 0
    assert multiply(7, 0) == 0

@pytest.mark.parametrize("a,b,expected", [
    (3.14, 2.71, 8),
    (-3.14, 2.71, 8),
    (3.14, -2.71, 8),
    (-3.14, -2.71, 8),
    (0.0, 0.0, 0),
    (0.0, 5.0, 0),
    (7.0, 0.0, 0)
])
def test_multiply_float_numbers(a, b, expected):
    assert multiply(a, b) == expected

def test_multiply_non_numeric_input():
    with pytest.raises(TypeError):
        multiply("a", "b")
    with pytest.raises(TypeError):
        multiply([1, 2], [3, 4])
    with pytest.raises(TypeError):
        multiply(None, 5)
    with pytest.raises(TypeError):
        multiply(5, None)