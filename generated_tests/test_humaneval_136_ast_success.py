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

def test_only_positive_numbers():
    assert largest_smallest_integers([2, 4, 1, 3]) == (None, 1)

def test_only_negative_numbers():
    assert largest_smallest_integers([-2, -4, -1, -3]) == (-1, None)

def test_mixed_numbers():
    assert largest_smallest_integers([-2, -4, 1, 3, -1, -3, 2]) == (-1, 1)

def test_zero_with_other_numbers():
    assert largest_smallest_integers([-2, 0, 2]) == (-2, 2)

def test_single_positive():
    assert largest_smallest_integers([5]) == (None, 5)

def test_single_negative():
    assert largest_smallest_integers([-5]) == (-5, None)

def test_only_zeros():
    assert largest_smallest_integers([0, 0, 0]) == (None, None)

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], (None, 1)),
    ([-1, -2, -3, -4, -5], (-1, None)),
    ([-10, -5, 0, 5, 10], (-5, 5)),
    ([0], (None, None)),
    ([-1, 1], (-1, 1)),
    ([99, -99], (-99, 99)),
    ([1.5, -1.5, 2.5, -2.5], (-1.5, 1.5)),
    ([-1, -1, -1, 1, 1, 1], (-1, 1))
])
def test_various_inputs(input_list, expected):
    assert largest_smallest_integers(input_list) == expected

@pytest.mark.parametrize("input_list", [
    [None],
    ["string"],
    [[1, 2], [3, 4]],
    [{}],
])
def test_invalid_inputs(input_list):
    with pytest.raises(Exception):
        largest_smallest_integers(input_list)

def test_boolean_inputs():
    result = largest_smallest_integers([True, False])
    assert result == (None, 1)