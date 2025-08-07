# Test cases for HumanEval/2
# Generated using Claude API



def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    return number % 1.0


# Generated test cases:
import pytest

def test_truncate_number_positive_float():
    assert truncate_number(3.5) == 0.5
    assert abs(truncate_number(7.9) - 0.9) < 1e-9
    assert truncate_number(12.0) == 0.0

def test_truncate_number_zero():
    assert truncate_number(0.0) == 0.0

def test_truncate_number_negative_float():
    with pytest.raises(ValueError):
        truncate_number(-3.5)

@pytest.mark.parametrize("input,expected", [
    (0.0, 0.0),
    (1.0, 0.0),
    (3.14, 0.14),
    (100.99, 0.99),
    (1000.0, 0.0)
])
def test_truncate_number_with_parametrize(input, expected):
    assert abs(truncate_number(input) - expected) < 1e-9

def test_truncate_number_with_non_float_input():
    with pytest.raises(TypeError):
        truncate_number("3.5")

def test_truncate_number_with_none_input():
    with pytest.raises(TypeError):
        truncate_number(None)