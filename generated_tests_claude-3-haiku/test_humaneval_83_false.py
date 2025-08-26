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
from solution import starts_one_ends
import pytest

def test_starts_one_ends_one():
    assert starts_one_ends(1) == 1

def test_starts_one_ends_two():
    assert starts_one_ends(2) == 18

def test_starts_one_ends_three():
    assert starts_one_ends(3) == 180

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 18),
    (3, 180),
    (4, 1800),
    (5, 18000),
    (6, 180000),
    (7, 1800000),
    (8, 18000000),
    (9, 180000000),
    (10, 1800000000)
])
def test_starts_one_ends_parametrized(input, expected):
    assert starts_one_ends(input) == expected

def test_starts_one_ends_negative():
    with pytest.raises(ValueError):
        starts_one_ends(-1)

def test_starts_one_ends_zero():
    with pytest.raises(ValueError):
        starts_one_ends(0)

def test_starts_one_ends_float():
    with pytest.raises(ValueError):
        starts_one_ends(1.5)