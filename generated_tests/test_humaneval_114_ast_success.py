# Test cases for HumanEval/114
# Generated using Claude API


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if (s < 0):
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = -max_sum
    return min_sum


# Generated test cases:
import pytest

def test_empty_array():
    with pytest.raises(ValueError):
        minSubArraySum([])

@pytest.mark.parametrize("nums,expected", [
    ([1, 2, 3], 1),
    ([-1, -2, -3], -6),
    ([1, -2, 3, -4], -4),
    ([5], 5),
    ([-5], -5),
    ([1, 1, 1], 1),
    ([-1, -1, -1], -3),
    ([1, -2, 1, -2], -3),
    ([0, 0, 0], 0),
    ([1, -1, 1, -1], -1),
    ([10, -5, 3, -2, 4, -8, 6], -8),
    ([-2, -3, 4, -1, -2, 1, 5, -3], -5),
    ([100, -200, 300, -400, 500], -400),
    ([1, 2, -3, 4, -5, 6, -7], -7),
])
def test_min_subarray_sum(nums, expected):
    assert minSubArraySum(nums) == expected

def test_all_positive():
    assert minSubArraySum([1, 2, 3, 4, 5]) == 1

def test_all_negative():
    assert minSubArraySum([-1, -2, -3, -4, -5]) == -15

def test_single_element():
    assert minSubArraySum([42]) == 42

def test_alternating():
    assert minSubArraySum([1, -1, 1, -1, 1, -1]) == -1

def test_large_numbers():
    assert minSubArraySum([1000000, -2000000, 3000000]) == -2000000

def test_zero_sum_sequence():
    assert minSubArraySum([1, -1, 2, -2, 3, -3]) == -3

def test_same_numbers():
    assert minSubArraySum([5, 5, 5, 5, 5]) == 5

def test_negative_sequence():
    assert minSubArraySum([-1, -2, -3, -2, -1]) == -9