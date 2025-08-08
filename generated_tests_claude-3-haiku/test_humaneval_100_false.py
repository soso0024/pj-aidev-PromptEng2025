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

def test_make_a_pile_positive_integers():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

def test_make_a_pile_zero():
    assert make_a_pile(0) == []

@pytest.mark.parametrize("n,expected", [
    (-1, ValueError),
    (-5, ValueError),
    (3.14, ValueError),
    ('abc', ValueError)
])
def test_make_a_pile_invalid_inputs(n, expected):
    with pytest.raises(expected):
        make_a_pile(n)

def make_a_pile(n):
    if n < 0 or not isinstance(n, int):
        raise ValueError("n must be a non-negative integer")
    return [n + 2*i for i in range(n)]