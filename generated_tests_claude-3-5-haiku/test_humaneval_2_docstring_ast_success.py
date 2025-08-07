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
    assert truncate_number(2.7) == pytest.approx(0.7)
    assert truncate_number(1.2) == pytest.approx(0.2)

def test_truncate_number_whole_numbers():
    assert truncate_number(4.0) == 0.0
    assert truncate_number(0.0) == 0.0

def test_truncate_number_negative_float():
    assert truncate_number(-3.5) == 0.5
    assert truncate_number(-2.7) == pytest.approx(0.3)

@pytest.mark.parametrize("input_number,expected", [
    (3.14, 0.14),
    (0.5, 0.5),
    (10.99, 0.99),
    (-5.25, 0.75)
])
def test_truncate_number_parametrized(input_number, expected):
    assert truncate_number(input_number) == pytest.approx(expected)

def test_truncate_number_large_numbers():
    assert truncate_number(1000.5) == 0.5
    assert truncate_number(9999.999) == pytest.approx(0.999)