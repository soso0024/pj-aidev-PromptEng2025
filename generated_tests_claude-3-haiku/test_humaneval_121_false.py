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
import pytest

def test_solution_empty_list():
    assert solution([]) == 0

def test_solution_all_even():
    assert solution([2, 4, 6, 8]) == 0

def test_solution_all_odd():
    assert solution([1, 3, 5, 7]) == 16

def test_solution_mixed():
    assert solution([1, 2, 3, 4, 5]) == 12

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5, 6], 12),
    ([1, 1, 1, 1, 1], 5),
    ([2, 2, 2, 2, 2], 0),
    ([-1, 2, -3, 4, -5], -4),
    ([0, 1, 0, 3, 0], 4)
])
def test_solution_parametrized(input, expected):
    assert solution(input) == expected

def test_solution_single_element():
    assert solution([1]) == 1

def test_solution_negative_numbers():
    assert solution([-1, -3, -5, -7]) == -8