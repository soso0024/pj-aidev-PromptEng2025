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

def test_truncate_number_positive_decimal():
    assert truncate_number(3.14) == pytest.approx(0.14)

def test_truncate_number_negative_decimal():
    assert truncate_number(-3.14) == pytest.approx(0.86)

def test_truncate_number_zero():
    assert truncate_number(0.0) == 0.0

def test_truncate_number_whole_number():
    assert truncate_number(5.0) == 0.0

def test_truncate_number_large_number():
    assert truncate_number(1234.5678) == pytest.approx(0.5678)

@pytest.mark.parametrize("input_value,expected", [
    (3.14, 0.14),
    (-3.14, 0.86),
    (0.0, 0.0),
    (5.0, 0.0),
    (1234.5678, 0.5678)
])
def test_truncate_number_parametrized(input_value, expected):
    assert truncate_number(input_value) == pytest.approx(expected)

def test_truncate_number_type_error():
    with pytest.raises(TypeError):
        truncate_number("not a number")

def test_truncate_number_complex():
    with pytest.raises(TypeError):
        truncate_number(1 + 2j)