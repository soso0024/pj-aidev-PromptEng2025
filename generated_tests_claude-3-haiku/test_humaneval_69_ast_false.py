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
    if not lst:
        return -1
    frq = [0] * (max(lst) + 1)
    for i in lst:
        if i >= 0:
            frq[i] += 1
    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    return ans

def test_search_empty_list():
    assert search([]) == -1

def test_search_single_element_list():
    assert search([5]) == 1

def test_search_all_unique_elements():
    assert search([1, 2, 3, 4, 5]) == 1

def test_search_repeated_elements():
    assert search([1, 1, 2, 2, 2, 3, 3, 3, 3]) == 3

def test_search_max_element_greater_than_length():
    assert search([1, 2, 3, 4, 10]) == 4

def test_search_negative_elements():
    assert search([-1, -2, -3]) == -1

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5], 1),
    ([1, 1, 2, 2, 2], 2),
    ([1, 1, 1, 2, 2, 2, 2], 2),
    ([1, 1, 1, 1, 2, 2, 2, 2, 2], 2),
    ([], -1),
    ([5], 1),
    ([-1, -2, -3], -1),
    ([1, 2, 3, 4, 10], 4)
])
def test_search_parametrized(input, expected):
    assert search(input) == expected