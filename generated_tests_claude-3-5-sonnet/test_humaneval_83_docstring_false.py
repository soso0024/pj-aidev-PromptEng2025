# Test cases for HumanEval/83
# Generated using Claude API


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1: return 1
    return 18 * (10 ** (n - 2))


# Generated test cases:
import pytest

def test_single_digit():
    assert starts_one_ends(1) == 1

def test_two_digits():
    assert starts_one_ends(2) == 18

def test_three_digits():
    assert starts_one_ends(3) == 180

def test_four_digits():
    assert starts_one_ends(4) == 1800

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 18),
    (3, 180),
    (4, 1800),
    (5, 18000)
])
def test_multiple_cases(n, expected):
    assert starts_one_ends(n) == expected

@pytest.mark.parametrize("invalid_input", [
    0,
    -1,
    -100
])
def test_invalid_inputs(invalid_input):
    with pytest.raises(ValueError):
        starts_one_ends(invalid_input)

def test_large_number():
    assert starts_one_ends(10) == 1800000000

@pytest.mark.parametrize("invalid_type", [
    "1",
    None,
    [],
    {}
])
def test_invalid_types(invalid_type):
    with pytest.raises((TypeError, ValueError)):
        starts_one_ends(invalid_type)

def test_float_input():
    with pytest.raises(ValueError):
        starts_one_ends(3.14)