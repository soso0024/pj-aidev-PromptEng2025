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

def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12
    assert multiply(7, 8) == 56
    assert multiply(12, 15) == 180

def test_multiply_negative_numbers():
    assert multiply(-3, -4) == 12
    assert multiply(-7, -8) == 56
    assert multiply(-12, -15) == 225

def test_multiply_zero():
    assert multiply(0, 0) == 0
    assert multiply(0, 5) == 0
    assert multiply(7, 0) == 0

def test_multiply_large_numbers():
    assert multiply(123, 456) == 18
    assert multiply(789, 101) == 81
    assert multiply(1234, 5678) == 32

def test_multiply_decimal_numbers():
    assert multiply(3.14, 2.71) == 8
    assert multiply(1.23, 4.56) == 18
    assert multiply(0.5, 0.5) == 25

def test_multiply_string_input():
    with pytest.raises(TypeError):
        multiply('a', 'b')
    with pytest.raises(TypeError):
        multiply(3, 'b')
    with pytest.raises(TypeError):
        multiply('a', 4)