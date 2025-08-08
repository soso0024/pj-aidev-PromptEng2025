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
    assert strange_sort_list([1, 2]) == [1, 2]

def test_basic_case():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]

def test_duplicate_values():
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]

def test_negative_numbers():
    assert strange_sort_list([-3, -2, -1, 0]) == [-3, 0, -2, -1]

def test_mixed_numbers():
    assert strange_sort_list([-2, 0, 3, -1, 2]) == [-2, 3, -1, 2, 0]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([], []),
    ([1], [1]),
    ([5, 5, 5], [5, 5, 5]),
    ([-1, -2, -3], [-3, -1, -2]),
    ([0, 1, 0, 1], [0, 1, 0, 1])
])
def test_strange_sort_parametrized(input_list, expected):
    assert strange_sort_list(input_list.copy()) == expected

def test_large_numbers():
    assert strange_sort_list([1000, 999, 998, 997]) == [997, 1000, 998, 999]

def test_reversed_list():
    assert strange_sort_list([4, 3, 2, 1]) == [1, 4, 2, 3]

def test_already_sorted():
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]

def test_list_modification():
    original = [3, 1, 4, 2]
    result = strange_sort_list(original.copy())
    assert result == [1, 4, 2, 3]
    assert original == [3, 1, 4, 2]

@pytest.mark.parametrize("invalid_input", [
    "string",
    123,
    3.14,
    {"a": 1},
    (1, 2, 3)
])
def test_invalid_input_type(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        strange_sort_list(invalid_input)

def test_none_input():
    with pytest.raises((TypeError, AttributeError)):
        strange_sort_list(None)