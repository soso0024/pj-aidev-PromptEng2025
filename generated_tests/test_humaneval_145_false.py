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

def test_order_by_points_basic():
    assert order_by_points([1, 11, 2, 21]) == [1, 2, 11, 21]
    assert order_by_points([5, 15, 25, 35]) == [5, 15, 25, 35]

def test_order_by_points_negative():
    assert order_by_points([-1, -11, -2, -21]) == [-1, -2, -11, -21]
    assert order_by_points([-5, -15, -25, -35]) == [-5, -15, -25, -35]

def test_order_by_points_mixed():
    assert order_by_points([-1, 2, -3, 4]) == [-1, 2, -3, 4]
    assert order_by_points([10, -10, 20, -20]) == [-10, 10, -20, 20]

def test_order_by_points_zeros():
    assert order_by_points([0, 100, -100, 0]) == [0, 0, -100, 100]

def test_order_by_points_same_sum():
    assert order_by_points([11, 11, 11]) == [11, 11, 11]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 11, 2, 21], [1, 2, 11, 21]),
    ([5, 15, 25, 35], [5, 15, 25, 35]),
    ([-1, -11, -2, -21], [-1, -2, -11, -21]),
    ([0, 100, -100, 0], [0, 0, -100, 100]),
    ([99, -99, 1000, -1000], [0, -99, 99, 1000])
])
def test_order_by_points_parametrized(input_list, expected):
    assert order_by_points(input_list) == expected

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single():
    assert order_by_points([42]) == [42]

def test_order_by_points_large_numbers():
    assert order_by_points([1000000, 2000000, 3000000]) == [1000000, 2000000, 3000000]

def test_order_by_points_duplicate_values():
    assert order_by_points([1, 1, 2, 2, 3, 3]) == [1, 1, 2, 2, 3, 3]