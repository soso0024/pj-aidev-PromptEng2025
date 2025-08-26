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

def make_a_pile(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise TypeError("Input must be non-negative")
    return [n + 2*i for i in range(n)]

def test_make_a_pile_basic():
    assert make_a_pile(3) == [3, 5, 7]

def test_make_a_pile_zero():
    assert make_a_pile(0) == []

def test_make_a_pile_single():
    assert make_a_pile(1) == [1]

def test_make_a_pile_multiple():
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

@pytest.mark.parametrize("n,expected", [
    (0, []),
    (1, [1]),
    (3, [3, 5, 7]),
    (5, [5, 7, 9, 11, 13])
])
def test_make_a_pile_parametrized(n, expected):
    assert make_a_pile(n) == expected

def test_make_a_pile_negative():
    with pytest.raises(TypeError):
        make_a_pile(-1)

def test_make_a_pile_non_integer():
    with pytest.raises(TypeError):
        make_a_pile(3.5)

def test_make_a_pile_string():
    with pytest.raises(TypeError):
        make_a_pile('3')