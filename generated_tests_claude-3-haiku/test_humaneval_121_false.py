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
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)

@pytest.mark.parametrize("lst,expected", [
    ([1, 2, 3, 4, 5], 9),
    ([1, 3, 5, 7, 9], 15),
    ([], 0),
    ([2, 4, 6, 8], 0),
    ([-1, 2, -3, 4, -5], -4),
    ([1, 1, 1, 1, 1], 2),
    ([0, 1, 0, 1, 0], 2),
    ([1, 2, 3, 4, 5, 6], 9),
    ([1, 1, 2, 2, 3, 3], 4),
    ([1, 2, 3, 4, 5, 6, 7], 12)
])
def test_solution(lst, expected):
    assert solution(lst) == expected

def test_solution_empty_list():
    assert solution([]) == 0

def test_solution_all_even_numbers():
    assert solution([2, 4, 6, 8, 10]) == 0

def test_solution_all_odd_numbers():
    assert solution([1, 3, 5, 7, 9]) == 15

def test_solution_mixed_numbers():
    assert solution([1, 2, 3, 4, 5]) == 9

def test_solution_negative_numbers():
    assert solution([-1, -3, -5, 2, 4]) == -4