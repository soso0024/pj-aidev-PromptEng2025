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

def test_basic_list():
    assert solution([5, 8, 7, 1]) == 12
    assert solution([3, 3, 3, 3, 3]) == 9
    assert solution([30, 13, 24, 321]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], 9),
    ([2, 2, 2, 2, 2], 0),
    ([1, 1, 1, 1], 2),
    ([99, 2, 33, 4, 55], 187),
    ([1], 1),
    ([2], 0),
    ([1, 2], 1),
    ([1, 2, 3], 4),
])
def test_various_lists(input_list, expected):
    assert solution(input_list) == expected

@pytest.mark.parametrize("input_list", [
    [0, 0, 0, 0],
    [2, 4, 6, 8],
    [10, 20, 30, 40],
])
def test_lists_with_no_odd_numbers(input_list):
    assert solution(input_list) == 0

@pytest.mark.parametrize("input_list", [
    [1, 1, 1, 1],
    [3, 3, 3, 3],
    [5, 5, 5, 5],
])
def test_lists_with_all_odd_numbers(input_list):
    result = solution(input_list)
    assert result == sum(x for i, x in enumerate(input_list) if i % 2 == 0)

def test_large_numbers():
    assert solution([999999999, 2, 999999999, 4]) == 1999999998

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
])
def test_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        solution(invalid_input)

def test_single_element_lists():
    assert solution([1]) == 1
    assert solution([2]) == 0
    assert solution([99]) == 99

def test_negative_numbers():
    assert solution([-1, 2, -3, 4]) == -4
    assert solution([-5, -4, -3, -2, -1]) == -9

def test_empty_list():
    assert solution([]) == 0

def test_mixed_types():
    with pytest.raises(TypeError):
        solution([1, "2", 3])
    with pytest.raises(TypeError):
        solution([1.5, 2, 3])

def solution(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, int) for x in lst):
        raise TypeError("All elements must be integers")
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])