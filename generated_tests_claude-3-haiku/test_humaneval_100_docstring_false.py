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

@pytest.mark.parametrize("n,expected", [
    (3, [3, 5, 7]),
    (5, [5, 7, 9, 11, 13]),
    (1, [1]),
    (0, []),
    (-1, ValueError),
    (3.14, TypeError)
])
def test_make_a_pile(n, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            make_a_pile(n)
    else:
        assert make_a_pile(n) == expected

def make_a_pile(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    return [n + 2*i for i in range(n)]