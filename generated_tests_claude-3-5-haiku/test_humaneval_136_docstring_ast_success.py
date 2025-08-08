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

def test_largest_smallest_integers_normal_case():
    assert largest_smallest_integers([1, -2, 3, -4, 5]) == (-2, 1)

def test_largest_smallest_integers_only_positive():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)

def test_largest_smallest_integers_only_negative():
    assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-1, None)

def test_largest_smallest_integers_empty_list():
    assert largest_smallest_integers([]) == (None, None)

def test_largest_smallest_integers_zero_list():
    assert largest_smallest_integers([0]) == (None, None)

@pytest.mark.parametrize("input_list,expected", [
    ([1, -2, 3, -4, 5], (-2, 1)),
    ([2, 4, 1, 3, 5, 7], (None, 1)),
    ([-1, -2, -3, -4, -5], (-1, None)),
    ([], (None, None)),
    ([0], (None, None)),
    ([-10, -5, 0, 5, 10], (-5, 5))
])
def test_largest_smallest_integers_parametrized(input_list, expected):
    assert largest_smallest_integers(input_list) == expected
