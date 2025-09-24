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
    assert count_nums([123]) == 1

def test_single_negative_number():
    assert count_nums([-123]) == 1

def test_single_zero():
    assert count_nums([0]) == 0

def test_mixed_positive_negative():
    assert count_nums([1, -2, 3, -4]) == 2

def test_all_positive():
    assert count_nums([1, 2, 3, 4, 5]) == 5

def test_all_negative():
    assert count_nums([-1, -2, -3, -4, -5]) == 0

def test_multiple_zeros():
    assert count_nums([0, 0, 0]) == 0

def test_negative_with_positive_digit_sum():
    assert count_nums([-321]) == 0

def test_negative_with_negative_digit_sum():
    assert count_nums([-123]) == 1

def test_large_numbers():
    assert count_nums([12345, -67890, 98765]) == 3

def test_single_digit_numbers():
    assert count_nums([1, -1, 5, -9, 0]) == 2

def test_negative_single_digit():
    assert count_nums([-1, -2, -3]) == 0

def test_mixed_with_zeros():
    assert count_nums([0, 1, -1, 0, 2]) == 2

def test_negative_number_positive_sum():
    assert count_nums([-4321]) == 1

def test_negative_number_zero_sum():
    assert count_nums([-1111]) == 1

def test_complex_mixed_array():
    assert count_nums([12, -7, 100, -14, -230]) == 4

@pytest.mark.parametrize("arr,expected", [
    ([1], 1),
    ([-1], 0),
    ([0], 0),
    ([1, 2, 3], 3),
    ([-1, -2, -3], 0),
    ([1, -1, 2, -2], 2),
    ([123, -456, 789], 3),
    ([-321, -654], 1),
    ([10, -10, 20, -20], 2),
    ([999, -999], 2)
])
def test_parametrized_cases(arr, expected):
    assert count_nums(arr) == expected