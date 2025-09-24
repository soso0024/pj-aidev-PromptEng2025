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

def minSubArraySum(nums):
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

def test_minSubArraySum_example_cases():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6

def test_minSubArraySum_single_element():
    assert minSubArraySum([5]) == 5
    assert minSubArraySum([-5]) == -5
    assert minSubArraySum([0]) == 0

def test_minSubArraySum_all_positive():
    assert minSubArraySum([1, 2, 3, 4, 5]) == 1
    assert minSubArraySum([10, 20, 30]) == 10
    assert minSubArraySum([7]) == 7

def test_minSubArraySum_all_negative():
    assert minSubArraySum([-1, -2, -3, -4]) == -10
    assert minSubArraySum([-5, -1, -3]) == -9
    assert minSubArraySum([-10, -5, -2]) == -17

def test_minSubArraySum_mixed_values():
    assert minSubArraySum([1, -2, 3, -4, 5]) == -4
    assert minSubArraySum([-1, 2, -3, 4, -5]) == -5
    assert minSubArraySum([5, -10, 3, -2, 1]) == -10

def test_minSubArraySum_with_zeros():
    assert minSubArraySum([0, 0, 0]) == 0
    assert minSubArraySum([1, 0, -1, 0, 2]) == -1
    assert minSubArraySum([0, -5, 0, 3, 0]) == -5

def test_minSubArraySum_consecutive_negatives():
    assert minSubArraySum([1, -3, -2, 4]) == -5
    assert minSubArraySum([5, -1, -1, -1, 3]) == -3
    assert minSubArraySum([-2, -1, -3, -4, 1]) == -10

def test_minSubArraySum_large_values():
    assert minSubArraySum([1000, 2000, 1]) == 1
    assert minSubArraySum([-1000, -2000, -1]) == -3001
    assert minSubArraySum([1000, -5000, 2000]) == -5000

@pytest.mark.parametrize("nums,expected", [
    ([1], 1),
    ([-1], -1),
    ([1, 2], 1),
    ([-1, -2], -3),
    ([2, -1], -1),
    ([-2, 1], -2),
    ([1, -1, 1], -1),
    ([-1, 1, -1], -1),
    ([3, -4, 2, -1], -4),
    ([10, -5, -3, 8], -8)
])
def test_minSubArraySum_parametrized(nums, expected):
    assert minSubArraySum(nums) == expected
