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

def test_make_a_pile_odd_numbers():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(1) == [1]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

def test_make_a_pile_even_numbers():
    assert make_a_pile(2) == [2, 4]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]

def test_make_a_pile_single_level():
    assert make_a_pile(1) == [1]

def test_make_a_pile_larger_numbers():
    assert make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    assert make_a_pile(7) == [7, 9, 11, 13, 15, 17, 19]

@pytest.mark.parametrize("n,expected", [
    (1, [1]),
    (2, [2, 4]),
    (3, [3, 5, 7]),
    (4, [4, 6, 8, 10]),
    (5, [5, 7, 9, 11, 13]),
    (8, [8, 10, 12, 14, 16, 18, 20, 22])
])
def test_make_a_pile_parametrized(n, expected):
    assert make_a_pile(n) == expected

def test_make_a_pile_result_length():
    assert len(make_a_pile(1)) == 1
    assert len(make_a_pile(5)) == 5
    assert len(make_a_pile(10)) == 10

def test_make_a_pile_sequence_properties():
    result = make_a_pile(4)
    for i in range(1, len(result)):
        assert result[i] - result[i-1] == 2
    
    result = make_a_pile(7)
    for i in range(1, len(result)):
        assert result[i] - result[i-1] == 2

def test_make_a_pile_first_element():
    assert make_a_pile(1)[0] == 1
    assert make_a_pile(5)[0] == 5
    assert make_a_pile(10)[0] == 10

def test_make_a_pile_parity_preservation():
    odd_result = make_a_pile(3)
    for stone_count in odd_result:
        assert stone_count % 2 == 1
    
    even_result = make_a_pile(4)
    for stone_count in even_result:
        assert stone_count % 2 == 0
