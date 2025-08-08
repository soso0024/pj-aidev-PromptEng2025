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

def test_make_a_pile_basic():
    assert make_a_pile(1) == [1]
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

@pytest.mark.parametrize("n,expected", [
    (1, [1]),
    (2, [2, 4]),
    (3, [3, 5, 7]),
    (4, [4, 6, 8, 10]),
    (5, [5, 7, 9, 11, 13])
])
def test_make_a_pile_parametrized(n, expected):
    assert make_a_pile(n) == expected

def test_make_a_pile_empty():
    assert make_a_pile(0) == []

def test_make_a_pile_large_number():
    result = make_a_pile(100)
    assert len(result) == 100
    assert result[0] == 100
    assert result[-1] == 100 + 2 * 99

@pytest.mark.parametrize("invalid_input", [
    -1,
    -100,
    -999
])
def test_make_a_pile_negative_input(invalid_input):
    assert make_a_pile(invalid_input) == []

def test_make_a_pile_type_check():
    with pytest.raises(TypeError):
        make_a_pile("3")
    with pytest.raises(TypeError):
        make_a_pile([1, 2, 3])
    with pytest.raises(TypeError):
        make_a_pile(None)
    with pytest.raises(TypeError):
        make_a_pile(3.14)
