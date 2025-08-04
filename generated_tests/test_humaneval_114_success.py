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

def test_minSubArraySum_empty_list():
    with pytest.raises(ValueError):
        minSubArraySum([])

@pytest.mark.parametrize("nums,expected", [
    ([1, 2, 3], 1),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], -5),
    ([5], 5),
    ([-1], -1),
    ([1, -1, 1, -1], -1),
    ([-1, -2, -3, -4], -10),
    ([1, 1, 1, 1], 1),
    ([-1, -1, 2, -1, -1], -2),
    ([0, 0, 0], 0),
    ([1, -2, 3, -4, 5, -6], -6),
    ([100, -101, 200, -201], -201),
    ([1, 2, -5, 4, 5], -5)
])
def test_minSubArraySum_various_inputs(nums, expected):
    assert minSubArraySum(nums) == expected

def test_minSubArraySum_single_zero():
    assert minSubArraySum([0]) == 0

def test_minSubArraySum_alternating():
    assert minSubArraySum([1, -1, 1, -1, 1, -1]) == -1

def test_minSubArraySum_all_positive():
    assert minSubArraySum([1, 2, 3, 4, 5]) == 1

def test_minSubArraySum_all_negative():
    assert minSubArraySum([-1, -2, -3, -4, -5]) == -15

def test_minSubArraySum_large_numbers():
    assert minSubArraySum([1000000, -1000001, 1000000]) == -1000001

def test_minSubArraySum_repeated_numbers():
    assert minSubArraySum([2, 2, 2, -6, 2, 2]) == -6