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
    assert make_a_pile(7) == [7, 9, 11, 13, 15, 17, 19]

@pytest.mark.parametrize("n,expected", [
    (1, [1]),
    (2, [2, 4]),
    (4, [4, 6, 8, 10]),
    (6, [6, 8, 10, 12, 14, 16])
])
def test_make_a_pile_with_parametrize(n, expected):
    assert make_a_pile(n) == expected

def test_make_a_pile_zero_input():
    with pytest.raises(ValueError):
        make_a_pile(0)

def test_make_a_pile_negative_input():
    with pytest.raises(ValueError):
        make_a_pile(-3)

def make_a_pile(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    return [n + 2*i for i in range(n)]
