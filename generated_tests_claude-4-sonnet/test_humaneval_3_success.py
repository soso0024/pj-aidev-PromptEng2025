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

@pytest.mark.parametrize("operations,expected", [
    ([], False),
    ([1, 2, 3], False),
    ([1, 2, -4], True),
    ([-1], True),
    ([0], False),
    ([0, 0, 0], False),
    ([5, -3, -1, -1], False),
    ([10, -5, -3, -2], False),
    ([1, -1, 1, -1], False),
    ([100, -50, -25, -25], False),
    ([100, -50, -25, -26], True),
    ([-5, 10, -3, -2], True),
    ([-5, 10, -6], True),
    ([0, -1], True),
    ([1, 0, -1], False),
    ([2, -1, -1], False),
    ([2, -1, -2], True),
    ([1000000, -999999], False),
    ([1000000, -1000001], True),
    ([-1000000], True)
])
def test_below_zero_parametrized(operations, expected):
    assert below_zero(operations) == expected

def test_below_zero_empty_list():
    assert below_zero([]) == False

def test_below_zero_single_positive():
    assert below_zero([5]) == False

def test_below_zero_single_negative():
    assert below_zero([-1]) == True

def test_below_zero_single_zero():
    assert below_zero([0]) == False

def test_below_zero_all_positive():
    assert below_zero([1, 2, 3, 4, 5]) == False

def test_below_zero_all_negative():
    assert below_zero([-1, -2, -3]) == True

def test_below_zero_mixed_never_negative():
    assert below_zero([10, -5, -3, -1]) == False

def test_below_zero_mixed_goes_negative():
    assert below_zero([5, -10]) == True

def test_below_zero_goes_negative_then_positive():
    assert below_zero([1, -2, 5]) == True

def test_below_zero_exactly_zero():
    assert below_zero([5, -5]) == False

def test_below_zero_large_numbers():
    assert below_zero([1000000, -500000, -500000]) == False

def test_below_zero_large_numbers_negative():
    assert below_zero([1000000, -500000, -500001]) == True