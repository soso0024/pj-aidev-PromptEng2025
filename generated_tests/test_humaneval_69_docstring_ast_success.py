# Test cases for HumanEval/69
# Generated using Claude API


def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''

    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1;

    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    
    return ans


# Generated test cases:
import pytest

@pytest.mark.parametrize("input_list,expected", [
    ([4, 1, 2, 2, 3, 1], 2),
    ([1, 2, 2, 3, 3, 3, 4, 4, 4], 3),
    ([5, 5, 4, 4, 4], -1),
    ([1], 1),
    ([1, 1], 1),
    ([2, 2], 2),
    ([3, 3, 3], 3),
    ([1, 1, 1, 1], 1),
    ([5], -1),
    ([10, 10, 10, 10, 10], -1),
    ([1, 2, 3, 4, 5], 1),
    ([2, 2, 1, 1], 2),
    ([3, 3, 3, 2, 2, 1], 3),
    ([1, 1, 2, 2, 2, 3, 3, 3, 3], 3),
    ([5, 4, 3, 2, 1], 1)
])
def test_search_parametrized(input_list, expected):
    assert search(input_list) == expected

def test_search_single_element():
    assert search([1]) == 1
    assert search([2]) == -1

def test_search_all_same_numbers():
    assert search([2, 2, 2]) == 2
    assert search([4, 4, 4, 4]) == 4
    assert search([5, 5]) == -1

def test_search_increasing_sequence():
    assert search([1, 2, 3, 4, 5]) == 1

def test_search_decreasing_sequence():
    assert search([5, 4, 3, 2, 1]) == 1

def test_search_repeated_numbers():
    assert search([1, 1, 1, 2, 2, 2, 3, 3]) == 2

@pytest.mark.parametrize("input_list", [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
])
def test_search_large_lists(input_list):
    result = search(input_list)
    assert isinstance(result, int)
    assert result >= -1

def test_search_with_max_frequency():
    assert search([1, 1, 1, 1, 1]) == 1
    assert search([2, 2, 2, 2]) == 2
    assert search([3, 3, 3]) == 3
