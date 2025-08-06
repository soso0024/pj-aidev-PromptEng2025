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

def test_next_smallest_basic():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2

def test_next_smallest_empty():
    assert next_smallest([]) is None

def test_next_smallest_single_element():
    assert next_smallest([1]) is None

def test_next_smallest_duplicates():
    assert next_smallest([1, 1, 1]) is None
    assert next_smallest([1, 2, 2, 2]) == 2
    assert next_smallest([3, 3, 1, 1, 2, 2]) == 2

def test_next_smallest_negative_numbers():
    assert next_smallest([-1, -2, -3]) == -2
    assert next_smallest([-3, -2, -1]) == -2

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], 2),
    ([5, 4, 3, 2, 1], 2),
    ([], None),
    ([1], None),
    ([1, 1], None),
    ([1, 1, 2, 2], 2),
    ([-1, -2, -3], -2),
    ([0, 0, 1, 1], 1),
    ([1.5, 2.5, 1.0], 1.5),
    ([10, 10, 10], None),
])
def test_next_smallest_parametrized(input_list, expected):
    assert next_smallest(input_list) == expected

def test_next_smallest_floats():
    assert next_smallest([1.5, 1.0, 2.0]) == 1.5
    assert next_smallest([1.0, 1.0, 2.0]) == 2.0

def test_next_smallest_mixed_numbers():
    assert next_smallest([1, 2.5, -1, 0]) == 0
    assert next_smallest([-1.5, -2, 0, 1]) == -1.5

def test_next_smallest_large_numbers():
    assert next_smallest([1000000, 999999, 1000001]) == 1000000
    assert next_smallest([2**31, 2**30, 2**32]) == 2**31
