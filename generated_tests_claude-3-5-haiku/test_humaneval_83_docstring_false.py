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

def starts_one_ends(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise TypeError("Input must be a positive integer")
    if n == 1:
        return 1
    return 18 * (10 ** (n - 2))

def test_starts_one_ends_single_digit():
    assert starts_one_ends(1) == 1

def test_starts_one_ends_two_digits():
    assert starts_one_ends(2) == 18

def test_starts_one_ends_three_digits():
    assert starts_one_ends(3) == 180

def test_starts_one_ends_five_digits():
    assert starts_one_ends(5) == 18000

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 18),
    (3, 180),
    (4, 1800),
    (5, 18000),
    (6, 180000)
])
def test_starts_one_ends_multiple_cases(n, expected):
    assert starts_one_ends(n) == expected

def test_starts_one_ends_large_number():
    assert starts_one_ends(10) == 18000000000

def test_starts_one_ends_zero_input():
    with pytest.raises(TypeError):
        starts_one_ends(0)

def test_starts_one_ends_negative_input():
    with pytest.raises(TypeError):
        starts_one_ends(-1)

def test_starts_one_ends_float_input():
    with pytest.raises(TypeError):
        starts_one_ends(2.5)