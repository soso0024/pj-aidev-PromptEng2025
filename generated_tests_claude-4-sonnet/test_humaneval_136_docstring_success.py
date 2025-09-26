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

def largest_smallest_integers(lst):
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)

@pytest.mark.parametrize("input_list,expected", [
    ([2, 4, 1, 3, 5, 7], (None, 1)),
    ([], (None, None)),
    ([0], (None, None)),
    ([-1, -2, -3], (-1, None)),
    ([1, 2, 3], (None, 1)),
    ([-5, -10, -1, 3, 8, 2], (-1, 2)),
    ([0, 0, 0], (None, None)),
    ([-1], (-1, None)),
    ([1], (None, 1)),
    ([-100, -50, -1, 0, 1, 50, 100], (-1, 1)),
    ([-5, -3, -8, -1], (-1, None)),
    ([10, 5, 20, 1], (None, 1)),
    ([-1, 0, 1], (-1, 1)),
    ([0, -5, 0, 10, 0], (-5, 10)),
    ([-2, -4, -6, 2, 4, 6], (-2, 2))
])
def test_largest_smallest_integers(input_list, expected):
    assert largest_smallest_integers(input_list) == expected

def test_empty_list():
    assert largest_smallest_integers([]) == (None, None)

def test_only_zeros():
    assert largest_smallest_integers([0, 0, 0, 0]) == (None, None)

def test_single_negative():
    assert largest_smallest_integers([-42]) == (-42, None)

def test_single_positive():
    assert largest_smallest_integers([42]) == (None, 42)

def test_mixed_with_zero():
    assert largest_smallest_integers([-10, 0, 10]) == (-10, 10)

def test_large_numbers():
    assert largest_smallest_integers([-1000000, 1000000]) == (-1000000, 1000000)

def test_duplicate_values():
    assert largest_smallest_integers([-5, -5, -5, 3, 3, 3]) == (-5, 3)
