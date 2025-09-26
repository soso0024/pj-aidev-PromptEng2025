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
    return sorted(nums, key=digits_sum)

def digits_sum(n):
    neg = 1
    if n < 0: n, neg = -n, -1 
    n = [int(i) for i in str(abs(n))]
    n[0] = n[0] * neg
    return sum(n)

def test_order_by_points():
    assert order_by_points([1, -1, -42, 42]) == [-42, -1, 1, 42]
    assert order_by_points([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert order_by_points([-1, -2, -3, -4]) == [-4, -3, -2, -1]
    assert order_by_points([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert order_by_points([10, 20, 30, 40]) == [10, 20, 30, 40]
    assert order_by_points([-10, -20, -30, -40]) == [-40, -30, -20, -10]
    assert order_by_points([100, -100, 200, -200]) == [-200, -100, 100, 200]
    assert order_by_points([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert order_by_points([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    assert order_by_points([]) == []

def test_digits_sum():
    assert digits_sum(1) == 1
    assert digits_sum(-1) == -1
    assert digits_sum(0) == 0
    assert digits_sum(10) == 1
    assert digits_sum(-10) == -1
    assert digits_sum(100) == 1
    assert digits_sum(-100) == -1
    assert digits_sum(123) == 6
    assert digits_sum(-123) == -6
    assert digits_sum(1000) == 1
    assert digits_sum(-1000) == -1

@pytest.mark.parametrize("input,expected", [
    ([1, -1, -42, 42], [-42, -1, 1, 42]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([-1, -2, -3, -4], [-4, -3, -2, -1]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([10, 20, 30, 40], [10, 20, 30, 40]),
    ([-10, -20, -30, -40], [-40, -30, -20, -10]),
    ([100, -100, 200, -200], [-200, -100, 100, 200]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]),
    ([], [])
])
def test_order_by_points_parametrize(input, expected):
    assert order_by_points(input) == expected

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (-1, -1),
    (0, 0),
    (10, 1),
    (-10, -1),
    (100, 1),
    (-100, -1),
    (123, 6),
    (-123, -6),
    (1000, 1),
    (-1000, -1)
])
def test_digits_sum_parametrize(input, expected):
    assert digits_sum(input) == expected