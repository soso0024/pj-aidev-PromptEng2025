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

def next_smallest(lst):
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]

def test_next_smallest_basic_cases():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2

def test_next_smallest_empty_list():
    assert next_smallest([]) is None

def test_next_smallest_single_element():
    assert next_smallest([1]) is None

def test_next_smallest_all_same_elements():
    assert next_smallest([1, 1]) is None
    assert next_smallest([5, 5, 5, 5]) is None

def test_next_smallest_two_unique_elements():
    assert next_smallest([1, 2]) == 2
    assert next_smallest([10, 5]) == 10

def test_next_smallest_with_duplicates():
    assert next_smallest([1, 1, 2, 2, 3, 3]) == 2
    assert next_smallest([5, 1, 1, 4, 4, 3, 2, 2]) == 2

def test_next_smallest_negative_numbers():
    assert next_smallest([-5, -1, -3, -2]) == -3
    assert next_smallest([-10, -10, -5]) == -5

def test_next_smallest_mixed_positive_negative():
    assert next_smallest([-1, 0, 1, 2]) == 0
    assert next_smallest([-5, 5, -3, 3]) == -3

def test_next_smallest_large_numbers():
    assert next_smallest([1000000, 999999, 1000001]) == 1000000

def test_next_smallest_unsorted_with_duplicates():
    assert next_smallest([3, 1, 4, 1, 5, 9, 2, 6, 5]) == 2

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], 2),
    ([5, 1, 4, 3, 2], 2),
    ([], None),
    ([1, 1], None),
    ([42], None),
    ([0, 0, 0], None),
    ([-1, -2, -3], -2),
    ([100, 1], 100)
])
def test_next_smallest_parametrized(input_list, expected):
    assert next_smallest(input_list) == expected
