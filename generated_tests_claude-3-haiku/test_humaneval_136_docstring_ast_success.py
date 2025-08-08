# Test cases for HumanEval/136
# Generated using Claude API


def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''

    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)


# Generated test cases:
import pytest

def test_largest_smallest_integers_empty_list():
    assert largest_smallest_integers([]) == (None, None)

def test_largest_smallest_integers_all_positive():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)

def test_largest_smallest_integers_all_negative():
    assert largest_smallest_integers([-2, -4, -1, -3, -5, -7]) == (-1, None)

def test_largest_smallest_integers_mixed():
    assert largest_smallest_integers([-2, 4, -1, 3, -5, 7]) == (-1, 3)

def test_largest_smallest_integers_all_zeros():
    assert largest_smallest_integers([0, 0, 0]) == (None, None)

def test_largest_smallest_integers_single_negative():
    assert largest_smallest_integers([-1]) == (-1, None)

def test_largest_smallest_integers_single_positive():
    assert largest_smallest_integers([1]) == (None, 1)

@pytest.mark.parametrize("input,expected", [
    ([2, 4, 1, 3, 5, 7], (None, 1)),
    ([-2, -4, -1, -3, -5, -7], (-1, None)),
    ([-2, 4, -1, 3, -5, 7], (-1, 3)),
    ([0, 0, 0], (None, None)),
    ([-1], (-1, None)),
    ([1], (None, 1)),
    ([], (None, None))
])
def test_largest_smallest_integers_parametrized(input, expected):
    assert largest_smallest_integers(input) == expected
