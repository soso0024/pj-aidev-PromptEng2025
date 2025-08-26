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

def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1

    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    
    return ans

def test_search_normal_cases():
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1

@pytest.mark.parametrize("input_list,expected", [
    ([1, 1], 1),
    ([2, 2, 2], 2),
    ([3, 3, 3, 3], 3),
    ([1, 2, 3, 4, 5], -1),
    ([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 10)
])
def test_search_parametrized(input_list, expected):
    assert search(input_list) == expected

def test_search_single_element():
    assert search([1]) == 1
    assert search([2]) == -1

def test_search_large_numbers():
    assert search([100, 100, 100, 100, 100]) == 100

def test_search_mixed_frequencies():
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4