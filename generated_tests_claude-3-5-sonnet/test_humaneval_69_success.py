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

def test_search_empty_list():
    with pytest.raises(ValueError):
        search([])

def test_search_single_element():
    assert search([1]) == 1
    assert search([2]) == -1

def test_search_basic_cases():
    assert search([1, 2, 2, 3, 4, 2]) == 2
    assert search([1, 1, 1, 1]) == 1
    assert search([5, 5, 5, 5, 5]) == 5

def test_search_no_match():
    assert search([1, 1, 2]) == 1
    assert search([5]) == -1

def test_search_zero_included():
    assert search([0, 1, 2]) == 1
    assert search([0, 0, 0]) == -1

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 2], 2),
    ([1, 1, 1, 2, 2], 2),
    ([3, 3, 3, 3], 3),
    ([1, 4, 4, 4, 4], 4),
    ([1, 2, 3, 4, 5], 1),
    ([2, 2], 2),
    ([1], 1),
    ([2], -1),
    ([1, 1, 1, 1, 1], 1),
    ([5, 5, 5, 5, 5, 5], 5)
])
def test_search_parametrized(input_list, expected):
    assert search(input_list) == expected

def test_search_large_numbers():
    assert search([100, 100, 100, 100, 100]) == -1
    assert search([50, 50, 50, 50, 50]) == -1

def test_search_repeated_numbers():
    assert search([2, 2, 2, 2, 2, 2]) == 2
    assert search([3, 3, 3, 3, 3, 3, 3]) == 3

def test_search_mixed_sequence():
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
    assert search([1, 2, 3, 4, 4, 4, 4]) == 4

def test_search_ascending_sequence():
    assert search([1, 2, 3, 4, 5]) == 1

def test_search_descending_sequence():
    assert search([5, 4, 3, 2, 1]) == 1