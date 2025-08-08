# Test cases for HumanEval/104
# Generated using Claude API


def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)


# Generated test cases:
import pytest
from typing import Iterable

@pytest.mark.parametrize("x,expected", [
    ([15, 33, 1422, 1], [1, 15, 33]),
    ([152, 323, 1422, 10], []),
    ([1, 3, 5, 7, 9], [1, 3, 5, 7, 9]),
    ([11, 13, 15, 17, 19], [11, 13, 15, 17, 19]),
    ([0], []),
    ([-1, -3, -5, -7, -9], []),
    ([1.5, 3.7, 5.1, 7.9], []),
    ([None], []),
    ([], []),
])
def test_unique_digits(x, expected):
    assert isinstance(x, Iterable)
    assert isinstance(expected, list)
    
    from solution import unique_digits
    assert unique_digits(x) == expected

def test_unique_digits_empty_input():
    assert unique_digits([]) == []

def test_unique_digits_non_integer_input():
    with pytest.raises(ValueError):
        unique_digits([1, 2.3, 4])

def test_unique_digits_negative_input():
    assert unique_digits([-1, -3, -5, -7, -9]) == []