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
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(1) == [1]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

@pytest.mark.parametrize("input_n,expected", [
    (1, [1]),
    (2, [2, 4]),
    (3, [3, 5, 7]),
    (4, [4, 6, 8, 10]),
    (5, [5, 7, 9, 11, 13]),
    (6, [6, 8, 10, 12, 14, 16])
])
def test_make_a_pile_parametrized(input_n, expected):
    assert make_a_pile(input_n) == expected

def test_make_a_pile_large_number():
    assert len(make_a_pile(100)) == 100
    assert make_a_pile(100)[0] == 100
    assert make_a_pile(100)[-1] == 298

def test_make_a_pile_invalid_input():
    with pytest.raises(ValueError):
        make_a_pile(0)
    with pytest.raises(ValueError):
        make_a_pile(-1)
    with pytest.raises(ValueError):
        make_a_pile(-100)

def test_make_a_pile_type_error():
    with pytest.raises(TypeError):
        make_a_pile("3")
    with pytest.raises(TypeError):
        make_a_pile([1])
    with pytest.raises(TypeError):
        make_a_pile(None)

def test_make_a_pile_sequence_properties():
    result = make_a_pile(5)
    for i in range(len(result)-1):
        assert result[i+1] - result[i] == 2

def test_make_a_pile_return_type():
    result = make_a_pile(3)
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)