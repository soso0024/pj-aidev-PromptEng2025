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

def test_single_positive_element():
    assert minSubArraySum([5]) == 5

def test_single_negative_element():
    assert minSubArraySum([-3]) == -3

def test_single_zero_element():
    assert minSubArraySum([0]) == 0

def test_all_positive_numbers():
    assert minSubArraySum([1, 2, 3, 4]) == 1

def test_all_negative_numbers():
    assert minSubArraySum([-1, -2, -3, -4]) == -10

def test_mixed_positive_negative():
    assert minSubArraySum([2, 3, -1, -4, 5]) == -5

def test_mixed_with_zero():
    assert minSubArraySum([0, -1, 2, -3]) == -3

def test_all_zeros():
    assert minSubArraySum([0, 0, 0]) == 0

def test_negative_then_positive():
    assert minSubArraySum([-5, 1, 2, 3]) == -5

def test_positive_then_negative():
    assert minSubArraySum([1, 2, -10, 3]) == -10

def test_alternating_signs():
    assert minSubArraySum([1, -2, 3, -4, 5]) == -4

def test_large_negative_in_middle():
    assert minSubArraySum([1, 2, -100, 3, 4]) == -100

def test_consecutive_negatives():
    assert minSubArraySum([1, -2, -3, -1, 2]) == -6

def test_kadane_minimum_case():
    assert minSubArraySum([2, -1, -3, 4, -1, 2, 1, -5, 4]) == -5

def test_two_elements_both_positive():
    assert minSubArraySum([3, 7]) == 3

def test_two_elements_both_negative():
    assert minSubArraySum([-3, -7]) == -10

def test_two_elements_mixed():
    assert minSubArraySum([5, -8]) == -8

def test_longer_array_with_minimum_at_start():
    assert minSubArraySum([-10, 1, 2, 3, 4]) == -10

def test_longer_array_with_minimum_at_end():
    assert minSubArraySum([1, 2, 3, -15]) == -15

def test_minimum_subarray_in_middle():
    assert minSubArraySum([5, -2, -3, -1, 6]) == -6

def test_equal_elements():
    assert minSubArraySum([2, 2, 2, 2]) == 2

def test_equal_negative_elements():
    assert minSubArraySum([-2, -2, -2, -2]) == -8