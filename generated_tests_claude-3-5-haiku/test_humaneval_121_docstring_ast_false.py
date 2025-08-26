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
    if not lst:
        raise IndexError("List cannot be empty")
    return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])

def test_solution_normal_cases():
    assert solution([5, 8, 7, 1]) == 12
    assert solution([3, 3, 3, 3, 3]) == 9
    assert solution([30, 13, 24, 321]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([5, 8, 7, 1], 12),
    ([3, 3, 3, 3, 3], 9),
    ([30, 13, 24, 321], 0),
    ([1, 2, 3, 4, 5], 4),
    ([2, 4, 6, 8, 10], 0),
    ([1], 1),
    ([2], 0)
])
def test_solution_parametrized(input_list, expected):
    assert solution(input_list) == expected

def test_solution_single_element_odd_in_even_position():
    assert solution([0, 1]) == 1

def test_solution_single_element_even_in_even_position():
    assert solution([0, 2]) == 0

def test_solution_empty_list_raises_error():
    with pytest.raises(IndexError):
        solution([])