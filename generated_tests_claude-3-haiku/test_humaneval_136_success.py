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

@pytest.mark.parametrize("lst,expected", [
    ([1, 2, 3, -4, -5], (max([-4, -5]), 1)),
    ([-1, -2, -3, 4, 5], (max([-1, -2, -3]), 4)),
    ([0, 0, 0], (None, None)),
    ([], (None, None)),
    ([1], (None, 1)),
    ([-1], (-1, None))
])
def test_largest_smallest_integers(lst, expected):
    assert largest_smallest_integers(lst) == expected

def test_largest_smallest_integers_with_non_numeric_elements():
    with pytest.raises(TypeError):
        largest_smallest_integers([1, 2, 'a', -4, -5])

def largest_smallest_integers(lst):
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)
