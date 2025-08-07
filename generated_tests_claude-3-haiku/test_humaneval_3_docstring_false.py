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

@pytest.mark.parametrize("operations,expected", [
    ([1, 2, 3], False),
    ([1, 2, -4, 5], True),
    ([], False),
    ([0, 0, 0], False),
    ([-1, -2, -3], True),
    ([1, -2, 1], True),
    ([1, 1, -2, 1], True),
    ([1, 1, 1, -3], True),
    ([1, 1, 1, -1, -1], True),
    ([1, 1, 1, -1, 1], False)
])
def test_below_zero(operations, expected):
    assert below_zero(operations) == expected

def below_zero(operations: List[int]) -> bool:
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False