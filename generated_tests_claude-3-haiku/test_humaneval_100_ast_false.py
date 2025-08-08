# Test cases for HumanEval/100
# Generated using Claude API


def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """

    return [n + 2*i for i in range(n)]


# Generated test cases:
import pytest

def test_make_a_pile_positive_input():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

def test_make_a_pile_zero_input():
    assert make_a_pile(0) == []

def test_make_a_pile_negative_input():
    with pytest.raises(ValueError):
        make_a_pile(-3)

@pytest.mark.parametrize("input,expected", [
    (1, [1, 3]),
    (10, [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]),
    (0, [])
])
def test_make_a_pile_parameterized(input, expected):
    assert make_a_pile(input) == expected

def make_a_pile(n):
    if n < 0:
        raise ValueError("n must be a positive integer")
    return [n + 2*i for i in range(n)]