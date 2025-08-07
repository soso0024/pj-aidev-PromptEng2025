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

def test_below_zero_empty_operations():
    assert below_zero([]) == False

@pytest.mark.parametrize("operations,expected", [
    ([1, 2, 3], False),
    ([-1, -2, -3], True),
    ([1, -2, 3], True),
    ([-1, 2, -3], True),
    ([0, 0, 0], False)
])
def test_below_zero_normal_cases(operations, expected):
    assert below_zero(operations) == expected

def test_below_zero_single_operation():
    assert below_zero([1]) == False
    assert below_zero([-1]) == True

def test_below_zero_single_zero_operation():
    assert below_zero([0]) == False

def test_below_zero_type_error():
    with pytest.raises(TypeError):
        below_zero("invalid")