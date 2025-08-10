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
    assert next_smallest([3, 1, 4, 1, 5]) == 2

def test_next_smallest_negative_numbers():
    assert next_smallest([-3, -1, -5, -2]) == -3

def test_next_smallest_positive_numbers():
    assert next_smallest([10, 5, 8, 3, 7]) == 5

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5], 2),
    ([5, 1, 4, 3, 2], 2),
    ([10, 5, 3, 1, 2], 2),
    ([-5, -3, -1, 1, 3], -3),
    ([0, 0, 1, 1, 2], 1)
])
def test_next_smallest_various_inputs(input, expected):
    assert next_smallest(input) == expected

def test_next_smallest_type_error():
    with pytest.raises(TypeError):
        next_smallest(123)

def test_next_smallest_string_input():
    with pytest.raises(TypeError):
        next_smallest(['a', 'b', 'c'])

def next_smallest(lst):
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]