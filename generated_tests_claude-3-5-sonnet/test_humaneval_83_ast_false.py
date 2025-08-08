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

def test_starts_one_ends_single_digit():
    assert starts_one_ends(1) == 1

def test_starts_one_ends_two_digits():
    assert starts_one_ends(2) == 18

def test_starts_one_ends_three_digits():
    assert starts_one_ends(3) == 180

def test_starts_one_ends_four_digits():
    assert starts_one_ends(4) == 1800

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 18),
    (3, 180),
    (4, 1800),
    (5, 18000),
    (6, 180000)
])
def test_starts_one_ends_parametrized(n, expected):
    assert starts_one_ends(n) == expected

@pytest.mark.parametrize("invalid_input", [
    0,
    -1,
    -100
])
def test_starts_one_ends_negative_input(invalid_input):
    with pytest.raises((ValueError, TypeError)):
        starts_one_ends(invalid_input)

def test_starts_one_ends_float_input():
    with pytest.raises(TypeError):
        starts_one_ends(1.5)

def test_starts_one_ends_string_input():
    with pytest.raises(TypeError):
        starts_one_ends("3")

def test_starts_one_ends_none_input():
    with pytest.raises(TypeError):
        starts_one_ends(None)