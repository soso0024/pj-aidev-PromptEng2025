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
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    if n == 1:
        return 1
    return 18 * (10 ** (n - 2))

def test_starts_one_ends_base_case():
    assert starts_one_ends(1) == 1

def test_starts_one_ends_small_cases():
    assert starts_one_ends(2) == 18
    assert starts_one_ends(3) == 180
    assert starts_one_ends(4) == 1800

def test_starts_one_ends_larger_cases():
    assert starts_one_ends(5) == 18000
    assert starts_one_ends(10) == 18 * (10 ** 8)

@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 18),
    (3, 180),
    (4, 1800),
    (5, 18000),
    (6, 180000),
    (10, 18 * (10 ** 8))
])
def test_starts_one_ends_parametrized(n, expected):
    assert starts_one_ends(n) == expected

def test_starts_one_ends_zero_input():
    with pytest.raises(ValueError):
        starts_one_ends(0)

def test_starts_one_ends_negative_input():
    with pytest.raises(ValueError):
        starts_one_ends(-1)