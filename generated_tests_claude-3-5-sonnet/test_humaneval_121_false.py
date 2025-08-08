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

def test_empty_list():
    assert solution([]) == 0

def test_no_odd_numbers():
    assert solution([2, 4, 6, 8, 10]) == 0

def test_no_even_indices():
    assert solution([1, 1, 1, 1, 1]) == 9

def test_mixed_numbers():
    assert solution([1, 2, 3, 4, 5]) == 9

def test_single_element():
    assert solution([1]) == 1

def test_single_even_element():
    assert solution([2]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5, 6], 9),
    ([1, 1, 1, 1], 2),
    ([2, 1, 2, 1, 2], 4),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20),
    ([-1, -2, -3, -4, -5], -9),
    ([1, 2], 1),
    ([2, 1], 0),
])
def test_various_cases(input_list, expected):
    assert solution(input_list) == expected

@pytest.mark.parametrize("input_list", [
    ["1", "2", "3"],
    [None, 1, 2],
    [(1,), (2,), (3,)],
])
def test_invalid_inputs(input_list):
    with pytest.raises((TypeError, ValueError)):
        solution(input_list)

def test_large_list():
    large_list = list(range(1000))
    expected = sum([x for idx, x in enumerate(large_list) if idx % 2 == 0 and x % 2 == 1])
    assert solution(large_list) == expected