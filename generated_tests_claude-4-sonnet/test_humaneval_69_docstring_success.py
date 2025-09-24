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
        frq[i] += 1;

    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    
    return ans

@pytest.mark.parametrize("lst,expected", [
    ([4, 1, 2, 2, 3, 1], 2),
    ([1, 2, 2, 3, 3, 3, 4, 4, 4], 3),
    ([5, 5, 4, 4, 4], -1),
    ([1], 1),
    ([1, 1], 1),
    ([2, 2], 2),
    ([3, 3, 3], 3),
    ([1, 1, 1, 1, 1], 1),
    ([2, 2, 2, 2], 2),
    ([3, 3], -1),
    ([4, 4, 4], -1),
    ([1, 2, 3, 4, 5], 1),
    ([2, 3, 4, 5, 6], -1),
    ([1, 1, 2, 2, 2], 2),
    ([1, 1, 1, 2, 2, 2, 2], 2),
    ([1, 1, 1, 1, 2, 2, 2, 2, 2], 2),
    ([3, 3, 3, 4, 4, 4, 4], 4),
    ([5, 5, 5, 5, 5], 5),
    ([6, 6, 6, 6, 6, 6], 6),
    ([7, 7, 7, 7, 7, 7], -1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1),
    ([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 10),
    ([2, 2, 3, 3, 3, 4, 4, 4, 4], 4),
    ([1, 1, 1, 3, 3, 3], 3),
    ([2, 2, 4, 4, 4, 4], 4)
])
def test_search(lst, expected):
    assert search(lst) == expected

def test_search_single_element():
    assert search([1]) == 1
    assert search([2]) == -1
    assert search([5]) == -1

def test_search_all_same_valid():
    assert search([1, 1, 1]) == 1
    assert search([2, 2, 2]) == 2
    assert search([3, 3, 3, 3]) == 3

def test_search_all_same_invalid():
    assert search([4, 4, 4]) == -1
    assert search([5, 5, 5, 5]) == -1

def test_search_multiple_valid_returns_greatest():
    assert search([1, 1, 2, 2, 3, 3, 3]) == 3
    assert search([1, 1, 1, 2, 2, 2, 2]) == 2
    assert search([1, 1, 1, 1, 2, 2, 2, 2, 2]) == 2

def test_search_large_numbers():
    assert search([100] * 100) == 100
    assert search([50] * 49) == -1
    assert search([50] * 50) == 50
