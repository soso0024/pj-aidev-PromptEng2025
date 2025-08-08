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

@pytest.mark.parametrize("n,expected", [
    (1, [1]),
    (2, [2, 4]),
    (3, [3, 5, 7]),
    (4, [4, 6, 8, 10]),
    (5, [5, 7, 9, 11, 13]),
])
def test_make_a_pile_parametrized(n, expected):
    assert make_a_pile(n) == expected

def test_make_a_pile_large_number():
    result = make_a_pile(10)
    assert len(result) == 10
    assert result[0] == 10
    assert result[-1] == 28

def test_make_a_pile_sequence():
    result = make_a_pile(6)
    for i in range(len(result)-1):
        if result[i] % 2 == 0:
            assert result[i+1] % 2 == 0
        else:
            assert result[i+1] % 2 != 0

def test_make_a_pile_arithmetic_progression():
    result = make_a_pile(5)
    differences = [result[i+1] - result[i] for i in range(len(result)-1)]
    assert all(diff == 2 for diff in differences)

def test_make_a_pile_type_error():
    with pytest.raises(TypeError):
        make_a_pile("3")
    with pytest.raises(TypeError):
        make_a_pile([1])
    with pytest.raises(TypeError):
        make_a_pile(3.14)

# Removed invalid input tests since the original function doesn't handle these cases