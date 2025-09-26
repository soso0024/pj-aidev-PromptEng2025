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
    if n == 1: return 1
    return 18 * (10 ** (n - 2))

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
    (6, 180000),
    (10, 1800000000)
])
def test_starts_one_ends_parametrized(n, expected):
    assert starts_one_ends(n) == expected

def test_starts_one_ends_large_number():
    assert starts_one_ends(15) == 18 * (10 ** 13)

def test_starts_one_ends_very_large_number():
    assert starts_one_ends(20) == 18 * (10 ** 18)
