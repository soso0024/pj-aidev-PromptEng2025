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
from functools import cmp_to_key

@pytest.mark.parametrize("nums,expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([-1, -2, -3, -4, -5], [-1, -2, -3, -4, -5]),
    ([10, 20, 30, 40, 50], [50, 40, 30, 20, 10]),
    ([100, 200, 300, 400, 500], [500, 400, 300, 200, 100]),
    ([11, 22, 33, 44, 55], [55, 44, 33, 22, 11]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ([1, -2, 3, -4, 5], [5, 3, 1, -2, -4]),
    ([10, -20, 30, -40, 50], [50, 30, 10, -20, -40]),
    ([100, -200, 300, -400, 500], [500, 300, 100, -200, -400]),
    ([11, -22, 33, -44, 55], [55, 33, 11, -22, -44]),
])
def test_order_by_points(nums, expected):
    assert order_by_points(nums) == expected

def test_order_by_points_empty_list():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([42]) == [42]

def test_order_by_points_duplicate_elements():
    assert order_by_points([10, 10, 20, 20]) == [10, 10, 20, 20]

def test_order_by_points_negative_and_positive_numbers():
    assert order_by_points([-10, 10, -20, 20]) == [-20, -10, 10, 20]

def digits_sum(n):
    neg = 1
    if n < 0: n, neg = -1 * n, -1 
    n = [int(i) for i in str(n)]
    n[0] = n[0] * neg
    return sum(n)

def order_by_points(nums):
    return sorted(nums, key=digits_sum)