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

def test_empty_list():
    assert next_smallest([]) is None

def test_single_element():
    assert next_smallest([5]) is None

def test_two_elements():
    assert next_smallest([3, 1]) == 3

def test_multiple_elements():
    assert next_smallest([4, 2, 8, 1, 9]) == 2

def test_duplicates():
    assert next_smallest([5, 5, 5, 5]) is None

def test_duplicates_with_different_values():
    assert next_smallest([3, 1, 3, 1, 2]) == 2

def test_negative_numbers():
    assert next_smallest([-5, -2, -8, -1]) == -5

def test_mixed_positive_negative():
    assert next_smallest([-3, 5, -1, 2]) == -1

def test_zeros():
    assert next_smallest([0, 0, 0]) is None

def test_zeros_with_other_numbers():
    assert next_smallest([0, -1, 1]) == 0

def test_floats():
    assert next_smallest([1.5, 2.7, 1.2, 3.8]) == 1.5

def test_all_same_duplicates():
    assert next_smallest([7, 7, 7, 7, 7]) is None

def test_large_numbers():
    assert next_smallest([1000000, 999999, 1000001]) == 1000000

def test_unsorted_input():
    assert next_smallest([10, 3, 7, 1, 15]) == 3

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2], 2),
    ([2, 1], 2),
    ([1], None),
    ([], None),
    ([5, 5], None),
    ([1, 2, 3], 2),
    ([3, 2, 1], 2),
    ([1, 1, 2, 2], 2)
])
def test_parametrized_cases(input_list, expected):
    assert next_smallest(input_list) == expected
