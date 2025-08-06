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

def test_solution_basic():
    assert solution([5, 8, 7, 1]) == 12
    assert solution([3, 3, 3, 3, 3]) == 9
    assert solution([30, 13, 24, 321]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], 9),
    ([2, 2, 2, 2], 0),
    ([1, 1, 1, 1], 2),
    ([99], 99),
    ([2, 4, 6, 8, 10], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 25),
    ([0, 1, 0, 1, 0], 0),
])
def test_solution_parametrized(input_list, expected):
    assert solution(input_list) == expected

@pytest.mark.parametrize("input_list", [
    [1000000001, 2, 3, 4, 5],
    [-1, -2, -3, -4, -5],
    [0, 0, 0, 0, 0],
])
def test_solution_edge_cases(input_list):
    result = solution(input_list)
    assert isinstance(result, int)

def test_solution_single_element():
    assert solution([1]) == 1
    assert solution([2]) == 0

def test_solution_all_odd():
    assert solution([1, 3, 5, 7, 9]) == 15

def test_solution_all_even():
    assert solution([2, 4, 6, 8, 10]) == 0

def test_solution_alternating():
    assert solution([1, 2, 3, 4, 5, 6]) == 9

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
])
def test_solution_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        solution(invalid_input)

def test_solution_empty_list():
    assert solution([]) == 0

def test_solution_mixed_types():
    with pytest.raises(TypeError):
        solution([1, "2", 3])
        solution([None, 2, 3])
    with pytest.raises(TypeError):
        solution([1.5, 2, 3])
        solution([True, 2, 3])