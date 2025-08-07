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

def test_below_zero_empty_list():
    assert below_zero([]) == False

def test_below_zero_positive_balance():
    assert below_zero([1, 2, 3]) == False

def test_below_zero_goes_negative():
    assert below_zero([1, -1, -2]) == True

def test_below_zero_starts_negative():
    assert below_zero([-1, 1, 2]) == True

@pytest.mark.parametrize("operations,expected", [
    ([], False),
    ([1, 2, 3], False),
    ([1, -1, -2], True),
    ([-1, 1, 2], True),
    ([0, 0, 0], False),
    ([-1, -2, -3], True),
    ([100, -50, -60], True),
    ([10, 20, -40, -50], True)
])
def test_below_zero_parametrized(operations, expected):
    assert below_zero(operations) == expected

def test_below_zero_large_numbers():
    assert below_zero([1000, -2000]) == True

def test_below_zero_zero_balance():
    assert below_zero([0, 0, 0, -1]) == True
