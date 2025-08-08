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
    if n <= 0:
        raise TypeError("Input must be a positive integer")
    return [n + 2*i for i in range(n)]

def test_make_a_pile_basic_cases():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(1) == [1]

@pytest.mark.parametrize("n,expected", [
    (2, [2, 4]),
    (5, [5, 7, 9, 11, 13]),
    (6, [6, 8, 10, 12, 14, 16])
])
def test_make_a_pile_parametrized(n, expected):
    assert make_a_pile(n) == expected

def test_make_a_pile_single_level():
    assert make_a_pile(1) == [1]

def test_make_a_pile_large_input():
    result = make_a_pile(10)
    assert len(result) == 10
    assert result[0] == 10
    assert result[-1] == 10 + 2 * 9

def test_make_a_pile_zero_input():
    with pytest.raises(TypeError):
        make_a_pile(0)

def test_make_a_pile_negative_input():
    with pytest.raises(TypeError):
        make_a_pile(-1)