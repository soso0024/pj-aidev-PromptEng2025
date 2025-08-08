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
    ([0], False),
    ([-1], True),
    ([1, -1], False),
    ([1, -2], True),
    ([100, 100, -300, 100], True),
    ([1, 2, 3, -5, -1], True),
    ([10, -5, -4, -1], True),
    ([0, 0, 0, 0], False),
    ([1000000, -1000000], False),
    ([1, -1, 1, -1, 1], False),
    ([5, -3, 2, -6], True),
])
def test_below_zero(operations: List[int], expected: bool):
    assert below_zero(operations) == expected


def test_below_zero_empty_list():
    assert below_zero([]) is False


def test_below_zero_single_positive():
    assert below_zero([5]) is False


def test_below_zero_single_negative():
    assert below_zero([-5]) is True


def test_below_zero_zero_balance():
    assert below_zero([0, 0, 0]) is False


def test_below_zero_large_numbers():
    assert below_zero([1000000, 2000000, -4000000]) is True


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