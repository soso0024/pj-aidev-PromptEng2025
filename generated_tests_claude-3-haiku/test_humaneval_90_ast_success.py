# Test cases for HumanEval/90
# Generated using Claude API


def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]


# Generated test cases:
import pytest

def test_next_smallest_empty_list():
    assert next_smallest([]) is None

def test_next_smallest_single_element_list():
    assert next_smallest([5]) is None

def test_next_smallest_duplicate_elements():
    assert next_smallest([3, 1, 4, 1, 5]) == 3

def test_next_smallest_negative_numbers():
    assert next_smallest([-3, -1, 0, 2]) == -1

def test_next_smallest_sorted_list():
    assert next_smallest([1, 2, 3, 4, 5]) == 2

def test_next_smallest_unsorted_list():
    assert next_smallest([5, 2, 1, 4, 3]) == 2

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5], 2),
    ([5, 4, 3, 2, 1], 2),
    ([-5, -3, -1, 1, 3], -3),
    ([3, 1, 4, 1, 5], 3),
    ([], None),
    ([5], None)
])
def test_next_smallest_parametrized(input, expected):
    assert next_smallest(input) == expected

def next_smallest(lst):
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]
