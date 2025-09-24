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
from solution import search

@pytest.mark.parametrize("input_list,expected", [
    ([4, 1, 2, 2, 3, 1], 2),
    ([1, 2, 2, 3, 3, 3, 4, 4, 4], 3),
    ([5, 5, 4, 4, 4], -1),
    ([1, 1, 1], 1),
    ([2, 2], 2),
    ([1], -1),
    ([], -1),
    ([1, 1, 2, 2, 2, 3, 3, 3, 3], 3),
    ([4, 4, 4, 4], 4),
    ([1, 1, 1, 2, 2, 2, 2], 2)
])
def test_search(input_list, expected):
    assert search(input_list) == expected