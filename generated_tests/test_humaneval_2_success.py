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

def test_truncate_number_basic():
    assert truncate_number(3.14) == pytest.approx(0.14)
    assert truncate_number(2.0) == pytest.approx(0.0)

@pytest.mark.parametrize("number,expected", [
    (1.23, 0.23),
    (5.67, 0.67),
    (0.45, 0.45),
    (10.1, 0.1),
    (3.0, 0.0),
    (7.999, 0.999),
    (-1.75, 0.25),
    (-2.3, 0.7),
    (0.0, 0.0),
    (1.0, 0.0),
    (99.99, 0.99),
    (0.001, 0.001),
])
def test_truncate_number_parametrized(number, expected):
    assert truncate_number(number) == pytest.approx(expected)

def test_truncate_number_large_values():
    assert truncate_number(1000.123) == pytest.approx(0.123)
    assert truncate_number(999999.999) == pytest.approx(0.999)

def test_truncate_number_small_decimals():
    assert truncate_number(1.000001) == pytest.approx(0.000001)
    assert truncate_number(2.000000001) == pytest.approx(0.000000001)

@pytest.mark.parametrize("invalid_input", [
    "1.23",
    None,
    [],
    {},
])
def test_truncate_number_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        truncate_number(invalid_input)

def test_truncate_number_boolean():
    result = truncate_number(True)
    assert result == pytest.approx(0.0)

def test_truncate_number_float_precision():
    assert truncate_number(1.1 + 2.2) == pytest.approx(0.3, rel=1e-10)
    assert truncate_number(0.1 + 0.2) == pytest.approx(0.3, rel=1e-10)