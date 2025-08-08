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

def test_empty_list():
    assert largest_smallest_integers([]) == (None, None)

def test_only_zero():
    assert largest_smallest_integers([0]) == (None, None)

def test_only_positives():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)

def test_only_negatives():
    assert largest_smallest_integers([-2, -4, -1, -3, -5, -7]) == (-1, None)

def test_mixed_numbers():
    assert largest_smallest_integers([-2, -4, 1, 3, -5, 7]) == (-2, 1)

def test_single_positive():
    assert largest_smallest_integers([5]) == (None, 5)

def test_single_negative():
    assert largest_smallest_integers([-5]) == (-5, None)

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], (None, 1)),
    ([-1, -2, -3, -4, -5], (-1, None)),
    ([0, 0, 0], (None, None)),
    ([-1, 0, 1], (-1, 1)),
    ([1.5, -2.5, 3.5], (-2.5, 1.5)),
    ([], (None, None)),
    ([10**6, -10**6], (-10**6, 10**6)),
])
def test_parametrized_cases(input_list, expected):
    assert largest_smallest_integers(input_list) == expected

def test_with_duplicates():
    assert largest_smallest_integers([1, 1, -1, -1, 2, 2, -2, -2]) == (-1, 1)

def test_with_float_values():
    assert largest_smallest_integers([-1.5, -2.5, 1.5, 2.5]) == (-1.5, 1.5)

def test_with_large_numbers():
    assert largest_smallest_integers([-999999, 999999, -1, 1]) == (-1, 1)

def test_with_zero_and_numbers():
    assert largest_smallest_integers([-1, 0, 1]) == (-1, 1)

def test_single_zero():
    assert largest_smallest_integers([0]) == (None, None)

def test_multiple_zeros():
    assert largest_smallest_integers([0, 0, 0, 0]) == (None, None)
