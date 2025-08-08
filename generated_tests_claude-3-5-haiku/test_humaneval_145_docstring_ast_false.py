# Test cases for HumanEval/145
# Generated using Claude API


def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)


# Generated test cases:
import pytest

def order_by_points(nums):
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=lambda x: (digits_sum(x), nums.index(x)))

def test_order_by_points_empty_list():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([10, 2, 30, 4], [10, 2, 4, 30]),
    ([-1, -10, 1, 10], [-1, 1, -10, 10]),
    ([100, 2, 3, 4, 5], [100, 2, 3, 4, 5]),
    ([55, 23, 32, 46, 88], [23, 32, 46, 55, 88])
])
def test_order_by_points_various_inputs(input_list, expected):
    assert order_by_points(input_list) == expected

def test_order_by_points_negative_numbers():
    assert order_by_points([-15, -11, -5, -1]) == [-1, -5, -11, -15]

def test_order_by_points_zero_included():
    assert order_by_points([0, 10, 1, 100]) == [0, 1, 10, 100]