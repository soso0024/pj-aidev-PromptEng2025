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
    assert minSubArraySum([]) == None

def test_minSubArraySum_single_positive_element():
    assert minSubArraySum([5]) == 5

def test_minSubArraySum_single_negative_element():
    assert minSubArraySum([-5]) == -5

def test_minSubArraySum_all_positive_elements():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1

def test_minSubArraySum_all_negative_elements():
    assert minSubArraySum([-1, -2, -3]) == -6

def test_minSubArraySum_mixed_elements():
    assert minSubArraySum([2, -3, 4, -1, 2, -4]) == -4

def test_minSubArraySum_zero_elements():
    assert minSubArraySum([0, 0, 0]) == 0

def test_minSubArraySum_duplicate_elements():
    assert minSubArraySum([1, 1, -2, 1, 1]) == -2

@pytest.mark.parametrize("input,expected", [
    ([2, 3, 4, 1, 2, 4], 1),
    ([-1, -2, -3], -6),
    ([0, 0, 0], 0),
    ([1, 1, -2, 1, 1], -2)
])
def test_minSubArraySum_parametrized(input, expected):
    assert minSubArraySum(input) == expected

def minSubArraySum(nums):
    if not nums:
        return None
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