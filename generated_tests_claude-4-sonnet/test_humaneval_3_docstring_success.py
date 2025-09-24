# Test cases for HumanEval/3
# Generated using Claude API

from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """

    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False


# Generated test cases:
import pytest
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

def test_empty_list():
    assert below_zero([]) == False

def test_single_positive():
    assert below_zero([5]) == False

def test_single_negative():
    assert below_zero([-1]) == True

def test_single_zero():
    assert below_zero([0]) == False

def test_all_positive():
    assert below_zero([1, 2, 3, 4, 5]) == False

def test_all_negative():
    assert below_zero([-1, -2, -3]) == True

def test_mixed_never_below_zero():
    assert below_zero([1, 2, 3]) == False

def test_mixed_goes_below_zero():
    assert below_zero([1, 2, -4, 5]) == True

def test_goes_below_zero_then_recovers():
    assert below_zero([5, -10, 3]) == True

def test_reaches_zero_exactly():
    assert below_zero([5, -5]) == False

def test_reaches_zero_multiple_times():
    assert below_zero([3, -3, 2, -2]) == False

def test_large_positive_then_negative():
    assert below_zero([100, -50, -30, -25]) == True

def test_large_positive_then_larger_negative():
    assert below_zero([100, -150]) == True

def test_alternating_positive_negative():
    assert below_zero([10, -5, 8, -3, 2, -1]) == False

def test_alternating_goes_negative():
    assert below_zero([5, -10, 3, -2]) == True

def test_starts_negative_immediately():
    assert below_zero([-1, 10, 5]) == True

def test_zero_operations():
    assert below_zero([0, 0, 0, 0]) == False

def test_mixed_with_zeros():
    assert below_zero([5, 0, -3, 0, -1]) == False

def test_mixed_with_zeros_goes_negative():
    assert below_zero([2, 0, -5, 0, 1]) == True

@pytest.mark.parametrize("operations,expected", [
    ([], False),
    ([1], False),
    ([-1], True),
    ([0], False),
    ([1, 2, 3], False),
    ([1, 2, -4, 5], True),
    ([10, -5, -3, -1], False),
    ([10, -5, -3, -3], True),
    ([0, 0, 0], False),
    ([5, -5, 5, -5], False),
    ([1, -2, 1], True)
])
def test_parametrized_cases(operations, expected):
    assert below_zero(operations) == expected