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
    max_sum = float('-inf')
    s = 0
    for num in nums:
        s += num
        max_sum = max(max_sum, s)
        if s < 0:
            s = 0
    return -max_sum

def test_minSubArraySum_empty_list():
    assert minSubArraySum([]) == 0

def test_minSubArraySum_single_positive_number():
    assert minSubArraySum([5]) == -5

def test_minSubArraySum_single_negative_number():
    assert minSubArraySum([-5]) == 5

def test_minSubArraySum_all_positive_numbers():
    assert minSubArraySum([1, 2, 3, 4, 5]) == -15

def test_minSubArraySum_all_negative_numbers():
    assert minSubArraySum([-1, -2, -3, -4, -5]) == -15

def test_minSubArraySum_mixed_numbers():
    assert minSubArraySum([1, -2, 3, -4, 5]) == -3

def test_minSubArraySum_zero_sum():
    assert minSubArraySum([1, -1, 1, -1, 1]) == 0

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5], -15),
    ([-1, -2, -3, -4, -5], -15),
    ([1, -2, 3, -4, 5], -3),
    ([1, -1, 1, -1, 1], 0),
    ([], 0),
    ([5], -5),
    ([-5], 5)
])
def test_minSubArraySum_parametrized(input, expected):
    assert minSubArraySum(input) == expected