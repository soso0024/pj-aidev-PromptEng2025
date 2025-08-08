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

def test_solution_all_odd_in_even_positions():
    assert solution([5, 7, 9, 11]) == 21

def test_solution_all_even_in_even_positions():
    assert solution([2, 4, 6, 8]) == 0

def test_solution_mixed_even_and_odd():
    assert solution([5, 8, 7, 1]) == 12

def test_solution_all_odd():
    assert solution([3, 3, 3, 3, 3]) == 9

def test_solution_all_even():
    assert solution([30, 24, 18, 12]) == 0

@pytest.mark.parametrize("input,expected", [
    ([5, 8, 7, 1], 12),
    ([3, 3, 3, 3, 3], 9),
    ([30, 13, 24, 321], 0),
    ([], 0),
    ([5, 7, 9, 11], 21),
    ([2, 4, 6, 8], 0),
    ([3, 4, 5, 6], 8)
])
def test_solution_parametrize(input, expected):
    assert solution(input) == expected