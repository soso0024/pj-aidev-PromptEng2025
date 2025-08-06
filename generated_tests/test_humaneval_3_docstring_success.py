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
    ([], False),
    ([0], False),
    ([1], False),
    ([-1], True),
    ([1, 2, 3], False),
    ([1, 2, -4, 5], True),
    ([1, -2, 3, -4, 5], True),
    ([100, -50, -51], True),
    ([10, -5, -4, -1, -1], True),
    ([5, -3, 2, -1], False),
    ([1000, 2000, -3000], False),
    ([1, 1, 1, -2, -1], False),
    ([-100], True),
    ([50, -50], False),
    ([1, -1, 1, -1], False),
])
def test_below_zero(operations: List[int], expected: bool):
    result = below_zero(operations)
    assert result == expected


def test_below_zero_large_numbers():
    assert below_zero([1000000, -2000000]) == True
    assert below_zero([1000000, 2000000, -2999999]) == False


def test_below_zero_repeated_zeros():
    assert below_zero([0, 0, 0, 0]) == False


def test_below_zero_alternating():
    assert below_zero([1, -1, 1, -1, 1, -2]) == True


@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    [1, "2", 3],
])
def test_below_zero_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        below_zero(invalid_input)


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False