# Test cases for HumanEval/121
# Generated using Claude API


def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])


# Generated test cases:
from solution import solution
import pytest

@pytest.mark.parametrize("input_list,expected", [
    ([5, 8, 7, 1], 12),
    ([3, 3, 3, 3, 3], 9),
    ([30, 13, 24, 321], 0),
    ([], 0),
    ([1, 2, 3, 4, 5], 6),
    ([-1, -2, -3, -4, -5], -4),
    ([0, 1, 2, 3, 4, 5], 6),
    ([1, 1, 1, 1, 1], 2),
    ([2, 4, 6, 8, 10], 0),
    ([1, 3, 5, 7, 9], 16)
])
def test_solution(input_list, expected):
    assert solution(input_list) == expected

def test_empty_list():
    assert solution([]) == 0

def test_all_even_numbers():
    assert solution([2, 4, 6, 8, 10]) == 0

def test_all_odd_numbers():
    assert solution([1, 3, 5, 7, 9]) == 16