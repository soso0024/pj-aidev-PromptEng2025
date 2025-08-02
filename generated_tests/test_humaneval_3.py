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
    ([1], False),
    ([-1], True),
    ([1, -1], False),
    ([1, -2], True),
    ([10, -5, -4, -2], True),
    ([3, -2, 1, -4], True),
    ([1, 2, 3, 4], False),
    ([0], False),
    ([0, 0, 0], False),
    ([1, 1, -1, -1], False),
    ([100, -99], False),
    ([100, -101], True),
    ([-1, 1, -1], True),
    ([5, -3, 2, -6, 1], True),
])
def test_below_zero(operations: List[int], expected: bool):
    assert below_zero(operations) == expected

def test_below_zero_large_numbers():
    operations = [1000000, -999999, -2]
    assert below_zero(operations) == True

def test_below_zero_alternating():
    operations = [1, -1, 1, -1, 1, -1, 1]
    assert below_zero(operations) == False

def test_below_zero_zero_sum():
    operations = [5, -2, -3, 4, -4]
    assert below_zero(operations) == False

@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    [1, "2", 3],
])
def test_below_zero_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        below_zero(invalid_input)

def test_below_zero_float_input():
    with pytest.raises(TypeError):
        below_zero([1.5, 2, 3])

def test_below_zero_boolean_input():
    with pytest.raises(TypeError):
        below_zero([True, False])