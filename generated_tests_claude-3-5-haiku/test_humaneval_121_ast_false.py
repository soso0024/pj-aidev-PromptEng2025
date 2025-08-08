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

def test_solution_empty_list():
    assert solution([]) == 0

def test_solution_no_odd_indices_even_elements():
    assert solution([2, 4, 6, 8, 10]) == 0

def test_solution_mixed_list():
    assert solution([1, 2, 3, 4, 5]) == 4

def test_solution_all_odd_elements():
    assert solution([1, 3, 5, 7, 9]) == 9

def test_solution_negative_numbers():
    assert solution([-1, 2, -3, 4, -5]) == -4

def test_solution_single_element_list():
    assert solution([1]) == 1

def test_solution_single_even_element_list():
    assert solution([2]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([], 0),
    ([2, 4, 6, 8, 10], 0),
    ([1, 2, 3, 4, 5], 4),
    ([1, 3, 5, 7, 9], 9),
    ([-1, 2, -3, 4, -5], -4),
    ([1], 1),
    ([2], 0)
])
def test_solution_parametrized(input_list, expected):
    assert solution(input_list) == expected