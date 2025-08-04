# Test cases for HumanEval/73
# Generated using Claude API


def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans


# Generated test cases:
import pytest

def test_empty_array():
    assert smallest_change([]) == 0

def test_single_element():
    assert smallest_change([1]) == 0

def test_two_identical_elements():
    assert smallest_change([1, 1]) == 0

def test_two_different_elements():
    assert smallest_change([1, 2]) == 1

@pytest.mark.parametrize("input_arr,expected", [
    ([1, 2, 1], 0),
    ([1, 2, 2], 1),
    ([1, 1, 2], 1),
    ([1, 2, 3, 4], 2),
    ([1, 2, 2, 1], 0),
    ([1, 2, 3, 1], 1),
    ([1, 1, 1, 1, 1], 0),
    ([1, 2, 3, 2, 1], 0),
    ([1, 2, 3, 4, 5], 2),
    ([5, 4, 3, 2, 1], 2),
    (["a", "b", "c", "b", "a"], 0),
    (["a", "b", "c", "d", "e"], 2),
    ([True, False, True], 0),
    ([True, False, False], 1)
])
def test_various_arrays(input_arr, expected):
    assert smallest_change(input_arr) == expected

@pytest.mark.parametrize("input_arr", [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 3, 2, 1],
    ["a", "b", "c", "c", "b", "a"]
])
def test_even_length_arrays(input_arr):
    result = smallest_change(input_arr)
    assert isinstance(result, int)
    assert result >= 0

def test_large_array():
    large_arr = list(range(1000)) + list(range(999, -1, -1))
    assert smallest_change(large_arr) == 0

def test_all_same_elements():
    assert smallest_change([7] * 100) == 0

@pytest.mark.parametrize("input_arr", [
    None,
    42,
    3.14
])
def test_invalid_inputs(input_arr):
    with pytest.raises((TypeError, AttributeError)):
        smallest_change(input_arr)

def test_string_input():
    result = smallest_change(list("string"))
    assert isinstance(result, int)
    assert result >= 0