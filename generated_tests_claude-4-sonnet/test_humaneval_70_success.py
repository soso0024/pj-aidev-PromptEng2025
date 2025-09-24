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

def strange_sort_list(lst):
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res

def test_empty_list():
    assert strange_sort_list([]) == []

def test_single_element():
    assert strange_sort_list([5]) == [5]

def test_two_elements():
    assert strange_sort_list([3, 1]) == [1, 3]

def test_three_elements():
    assert strange_sort_list([1, 2, 3]) == [1, 3, 2]

def test_four_elements():
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]

def test_negative_numbers():
    assert strange_sort_list([-1, -5, -3]) == [-5, -1, -3]

def test_mixed_positive_negative():
    assert strange_sort_list([-2, 1, 3, -1]) == [-2, 3, -1, 1]

def test_duplicates():
    assert strange_sort_list([1, 2, 2, 3]) == [1, 3, 2, 2]

def test_already_sorted():
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]

def test_reverse_sorted():
    assert strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3]

def test_zero_included():
    assert strange_sort_list([0, 1, -1]) == [-1, 1, 0]

def test_large_numbers():
    assert strange_sort_list([1000, 999, 1001]) == [999, 1001, 1000]

def test_float_numbers():
    assert strange_sort_list([1.5, 2.5, 0.5]) == [0.5, 2.5, 1.5]

@pytest.mark.parametrize("input_list,expected", [
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([4, 3, 2, 1], [1, 4, 2, 3]),
    ([5, 6, 7, 8, 9], [5, 9, 6, 8, 7])
])
def test_parametrized_cases(input_list, expected):
    assert strange_sort_list(input_list) == expected

def test_modifies_original_list():
    original = [1, 2, 3]
    result = strange_sort_list(original)
    assert original == []
    assert result == [1, 3, 2]

def test_long_list():
    input_list = list(range(10))
    expected = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
    assert strange_sort_list(input_list) == expected
