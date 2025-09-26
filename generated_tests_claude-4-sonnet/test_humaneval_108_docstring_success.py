# Test cases for HumanEval/108
# Generated using Claude API


def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))


# Generated test cases:
import pytest

def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))

def test_empty_array():
    assert count_nums([]) == 0

def test_single_positive_number():
    assert count_nums([1]) == 1
    assert count_nums([123]) == 1
    assert count_nums([999]) == 1

def test_single_negative_number():
    assert count_nums([-1]) == 0
    assert count_nums([-123]) == 1
    assert count_nums([-999]) == 1

def test_single_zero():
    assert count_nums([0]) == 0

def test_mixed_numbers():
    assert count_nums([-1, 11, -11]) == 1
    assert count_nums([1, 1, 2]) == 3

def test_all_positive():
    assert count_nums([1, 2, 3, 4, 5]) == 5
    assert count_nums([10, 20, 30]) == 3

def test_all_negative():
    assert count_nums([-1, -2, -3]) == 0
    assert count_nums([-10, -20, -30]) == 0

def test_negative_with_positive_digit_sum():
    assert count_nums([-123]) == 1
    assert count_nums([-234]) == 1
    assert count_nums([-199]) == 1

def test_negative_with_zero_digit_sum():
    assert count_nums([-10]) == 0
    assert count_nums([-100]) == 0

def test_negative_with_negative_digit_sum():
    assert count_nums([-1]) == 0
    assert count_nums([-2]) == 0
    assert count_nums([-9]) == 0

def test_large_numbers():
    assert count_nums([123456789]) == 1
    assert count_nums([-123456789]) == 1

def test_multiple_zeros():
    assert count_nums([0, 0, 0]) == 0

@pytest.mark.parametrize("arr,expected", [
    ([], 0),
    ([0], 0),
    ([1], 1),
    ([-1], 0),
    ([1, 2, 3], 3),
    ([-1, -2, -3], 0),
    ([-123, 456, -789], 3),
    ([10, -10, 100, -100], 2),
    ([-12, -21, -30], 1),
])
def test_parametrized_cases(arr, expected):
    assert count_nums(arr) == expected