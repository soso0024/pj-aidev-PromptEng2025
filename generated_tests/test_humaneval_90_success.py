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

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], 2),
    ([5, 5, 5, 5], None),
    ([1], None),
    ([], None),
    ([3, 1, 2, 4, 5], 2),
    ([10, 10, 9, 8, 8, 7], 8),
    ([1.5, 2.5, 1.0], 1.5),
    ([-1, -2, -3], -2),
    ([0, 0, 0, 1], 1),
    ([2, 2, 1, 1, 3, 3], 2),
    ([float('inf'), 1, 2], 2),
    ([1, float('inf'), float('inf')], float('inf')),
    ([1.0, 1, 2, 2.0], 2),
    ([-1, -1, -2, -2], -1),
    ([100, 0, 50, 25, 75], 25)
])
def test_next_smallest_parametrize(input_list, expected):
    assert next_smallest(input_list) == expected

def test_next_smallest_with_strings():
    result = next_smallest(['a', 'b', 'c'])
    assert result == 'b'

def test_next_smallest_with_mixed_types():
    with pytest.raises(TypeError):
        next_smallest([1, 'a', 2])

def test_next_smallest_with_none():
    with pytest.raises(TypeError):
        next_smallest([1, None, 2])

def test_next_smallest_with_bool():
    assert next_smallest([True, False, True]) == True

def test_next_smallest_with_nested_lists():
    with pytest.raises(TypeError):
        next_smallest([[1, 2], [3, 4]])