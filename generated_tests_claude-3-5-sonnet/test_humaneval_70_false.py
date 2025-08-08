# Test cases for HumanEval/70
# Generated using Claude API


def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''

    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res


# Generated test cases:
import pytest

def test_empty_list():
    assert strange_sort_list([]) == []

def test_single_element():
    assert strange_sort_list([1]) == [1]

def test_two_elements():
    assert strange_sort_list([2, 1]) == [1, 2]

def test_duplicate_elements():
    assert strange_sort_list([3, 3, 3]) == [3, 3, 3]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([5, 2, 8, 1, 9], [1, 9, 2, 8, 5]),
    ([3, 1, 2, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ([10, 5, 15, 20], [5, 20, 10, 15]),
])
def test_various_lists(input_list, expected):
    assert strange_sort_list(input_list.copy()) == expected

def test_negative_numbers():
    assert strange_sort_list([-3, -1, -2, -4]) == [-4, -1, -3, -2]

def test_mixed_numbers():
    assert strange_sort_list([-2, 0, 3, -1, 2]) == [-2, 3, -1, 2, 0]

def test_float_numbers():
    assert strange_sort_list([1.5, 2.5, 1.1, 2.1]) == [1.1, 2.5, 1.5, 2.1]

def test_large_list():
    input_list = list(range(10, 0, -1))
    expected = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    assert strange_sort_list(input_list) == expected

def test_list_with_zeros():
    assert strange_sort_list([0, 0, 0, 1, -1]) == [-1, 1, 0, 0, 0]

@pytest.mark.parametrize("invalid_input", [
    "string",
    123,
    True,
    {'a': 1},
    (1, 2, 3)
])
def test_invalid_input_type(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        strange_sort_list(invalid_input)

def test_none_input():
    with pytest.raises((TypeError, AttributeError)):
        strange_sort_list(None)