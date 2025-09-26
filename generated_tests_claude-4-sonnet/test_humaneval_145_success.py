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
    return sorted(nums, key=digits_sum)

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]
    assert order_by_points([-5]) == [-5]
    assert order_by_points([0]) == [0]

def test_positive_numbers():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_all_positive():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_all_negative():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]

def test_mixed_signs():
    assert order_by_points([1, -1, 2, -2]) == [-2, -1, 1, 2]

def test_zero_included():
    assert order_by_points([0, 1, -1]) == [-1, 0, 1]

def test_same_digit_sum():
    assert order_by_points([10, 1]) == [10, 1]
    assert order_by_points([20, 11, 2]) == [20, 11, 2]

def test_multi_digit_numbers():
    assert order_by_points([123, 321, 132]) == [123, 321, 132]

def test_negative_multi_digit():
    assert order_by_points([-123, -321, -132]) == [-321, -123, -132]

def test_large_numbers():
    assert order_by_points([1000, 999, 1001]) == [1000, 1001, 999]

def test_negative_with_zero_first_digit():
    assert order_by_points([-10, -20, -30]) == [-30, -20, -10]

@pytest.mark.parametrize("nums,expected", [
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([0], [0]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([-5, -4, -3, -2, -1], [-5, -4, -3, -2, -1]),
    ([100, 10, 1], [100, 10, 1])
])
def test_parametrized_cases(nums, expected):
    assert order_by_points(nums) == expected

def test_duplicate_numbers():
    assert order_by_points([1, 1, 1]) == [1, 1, 1]
    assert order_by_points([-1, -1, -1]) == [-1, -1, -1]

def test_complex_case():
    result = order_by_points([1, 11, -1, -11, -12])
    expected = [-1, -11, 1, -12, 11]
    assert result == expected