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

def test_below_zero_empty_list():
    assert below_zero([]) == False

def test_below_zero_positive_balance():
    assert below_zero([10, 20, 30]) == False

def test_below_zero_negative_balance():
    assert below_zero([-10, 20, -30]) == True

def test_below_zero_balance_at_zero():
    assert below_zero([10, -10, 0]) == False

@pytest.mark.parametrize("operations,expected", [
    ([1, 2, -3, 4, -5], True),
    ([1, 2, 3, 4, 5], False),
    ([-1, -2, -3, -4, -5], True),
    ([0, 0, 0, 0, 0], False)
])
def test_below_zero_various_cases(operations, expected):
    assert below_zero(operations) == expected

def below_zero(operations: list[int]):
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False
