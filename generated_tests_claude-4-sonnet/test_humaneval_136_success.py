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

def test_empty_list():
    assert largest_smallest_integers([]) == (None, None)

def test_only_positive_numbers():
    assert largest_smallest_integers([1, 2, 3, 4, 5]) == (None, 1)

def test_only_negative_numbers():
    assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-1, None)

def test_mixed_positive_negative():
    assert largest_smallest_integers([-5, -2, 1, 3]) == (-2, 1)

def test_single_positive():
    assert largest_smallest_integers([42]) == (None, 42)

def test_single_negative():
    assert largest_smallest_integers([-42]) == (-42, None)

def test_with_zero():
    assert largest_smallest_integers([0]) == (None, None)

def test_mixed_with_zero():
    assert largest_smallest_integers([-3, 0, 5]) == (-3, 5)

def test_multiple_zeros():
    assert largest_smallest_integers([0, 0, 0]) == (None, None)

def test_duplicates():
    assert largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)

def test_large_numbers():
    assert largest_smallest_integers([-1000000, 1000000]) == (-1000000, 1000000)

def test_unsorted_list():
    assert largest_smallest_integers([5, -3, 8, -1, 2, -7]) == (-1, 2)

def test_all_same_negative():
    assert largest_smallest_integers([-5, -5, -5]) == (-5, None)

def test_all_same_positive():
    assert largest_smallest_integers([5, 5, 5]) == (None, 5)

@pytest.mark.parametrize("input_list,expected", [
    ([-1, 1], (-1, 1)),
    ([-10, -5, 10, 15], (-5, 10)),
    ([100, -100], (-100, 100)),
    ([-1, -2, -3, 1, 2, 3], (-1, 1))
])
def test_parametrized_cases(input_list, expected):
    assert largest_smallest_integers(input_list) == expected
