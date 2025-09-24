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
from typing import List
import pytest

def test_below_zero_empty_list():
    assert below_zero([]) is False

def test_below_zero_positive_operations():
    assert below_zero([1, 2, 3]) is False

def test_below_zero_negative_operations():
    assert below_zero([-1, -2, -3]) is True

def test_below_zero_mixed_operations():
    assert below_zero([1, 2, -4, 5]) is True

def test_below_zero_single_negative_operation():
    assert below_zero([1, 2, -3]) is True

def test_below_zero_single_positive_operation():
    assert below_zero([1]) is False

@pytest.mark.parametrize("operations,expected", [
    ([1, 2, 3], False),
    ([1, 2, -4, 5], True),
    ([-1, -2, -3], True),
    ([1], False),
    ([], False)
])
def test_below_zero_parametrized(operations: List[int], expected: bool):
    assert below_zero(operations) == expected