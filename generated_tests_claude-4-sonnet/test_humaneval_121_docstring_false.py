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

def solution(lst):
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])

def test_solution_basic_cases():
    assert solution([5, 8, 7, 1]) == 12
    assert solution([3, 3, 3, 3, 3]) == 9
    assert solution([30, 13, 24, 321]) == 0

def test_solution_single_element():
    assert solution([1]) == 1
    assert solution([2]) == 0
    assert solution([0]) == 0

def test_solution_two_elements():
    assert solution([1, 2]) == 1
    assert solution([2, 1]) == 2
    assert solution([3, 5]) == 3
    assert solution([4, 6]) == 0

def test_solution_all_odd_numbers():
    assert solution([1, 3, 5, 7, 9]) == 15
    assert solution([1, 3, 5]) == 6
    assert solution([7, 9, 11, 13]) == 18

def test_solution_all_even_numbers():
    assert solution([2, 4, 6, 8]) == 0
    assert solution([0, 2, 4]) == 0
    assert solution([10, 20, 30, 40, 50]) == 0

def test_solution_mixed_positions():
    assert solution([1, 2, 3, 4, 5, 6, 7, 8]) == 16
    assert solution([2, 1, 4, 3, 6, 5]) == 2
    assert solution([0, 1, 2, 3, 4, 5, 6, 7]) == 2

def test_solution_negative_numbers():
    assert solution([-1, -2, -3, -4]) == -4
    assert solution([-1, 2, -3, 4, -5]) == -9
    assert solution([-2, -4, -6, -8]) == 0

def test_solution_zero_included():
    assert solution([0, 1, 0, 3, 0]) == 0
    assert solution([1, 0, 3, 0, 5]) == 9
    assert solution([0, 0, 0, 0]) == 0

def test_solution_large_numbers():
    assert solution([101, 200, 303, 400]) == 404
    assert solution([1000, 1001, 1002, 1003]) == 0
    assert solution([999, 1000, 1001, 1002, 1003]) == 2003

@pytest.mark.parametrize("input_list,expected", [
    ([1], 1),
    ([2], 0),
    ([1, 2], 1),
    ([2, 1], 2),
    ([1, 2, 3], 4),
    ([2, 1, 4], 2),
    ([5, 8, 7, 1], 12),
    ([3, 3, 3, 3, 3], 9),
    ([30, 13, 24, 321], 0),
    ([-1, -2, -3], -4),
    ([0, 1, 2, 3, 4], 2)
])
def test_solution_parametrized(input_list, expected):
    assert solution(input_list) == expected