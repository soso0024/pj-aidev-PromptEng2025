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
    return [n + 2*i for i in range(n)]

def test_make_a_pile_basic_cases():
    assert make_a_pile(1) == [1]
    assert make_a_pile(2) == [2, 4]
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

def test_make_a_pile_zero():
    assert make_a_pile(0) == []

def test_make_a_pile_large_number():
    result = make_a_pile(10)
    expected = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    assert result == expected
    assert len(result) == 10

def test_make_a_pile_negative_numbers():
    assert make_a_pile(-1) == []
    assert make_a_pile(-5) == []

@pytest.mark.parametrize("n,expected", [
    (1, [1]),
    (2, [2, 4]),
    (3, [3, 5, 7]),
    (6, [6, 8, 10, 12, 14, 16]),
    (0, []),
])
def test_make_a_pile_parametrized(n, expected):
    assert make_a_pile(n) == expected

def test_make_a_pile_properties():
    n = 7
    result = make_a_pile(n)
    
    # Check length
    assert len(result) == n
    
    # Check first element
    assert result[0] == n
    
    # Check arithmetic progression (difference of 2)
    for i in range(1, len(result)):
        assert result[i] - result[i-1] == 2

def test_make_a_pile_return_type():
    assert isinstance(make_a_pile(1), list)
    assert isinstance(make_a_pile(0), list)
    assert isinstance(make_a_pile(5), list)

def test_make_a_pile_elements_type():
    result = make_a_pile(3)
    for element in result:
        assert isinstance(element, int)
