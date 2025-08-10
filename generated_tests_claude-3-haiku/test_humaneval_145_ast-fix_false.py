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
        if n < 0:
            n, neg = -n, -1
        n = [int(i) for i in str(abs(n))]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)

def test_order_by_points():
    assert order_by_points([1, -1, -42, 42, 0, 100, -100]) == [-100, -42, -1, 0, 1, 42, 100]
    assert order_by_points([]) == []
    assert order_by_points([1, 2, 3]) == [1, 2, 3]
    assert order_by_points([-1, -2, -3]) == [-3, -2, -1]
    assert order_by_points([10, 20, 30]) == [10, 20, 30]
    assert order_by_points([-10, -20, -30]) == [-30, -20, -10]
    assert order_by_points([11, 22, 33]) == [11, 22, 33]
    assert order_by_points([-11, -22, -33]) == [-33, -22, -11]
    assert order_by_points([100, -100, 200, -200]) == [-200, -100, 100, 200]
    assert order_by_points([0, 0, 0]) == [0, 0, 0]
    assert order_by_points([1, 1, 1]) == [1, 1, 1]
    assert order_by_points([-1, -1, -1]) == [-1, -1, -1]