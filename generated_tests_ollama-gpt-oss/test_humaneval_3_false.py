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
from typing import Iterable

def below_zero(operations):
    try:
        iterator = iter(operations)
    except TypeError:
        raise TypeError("operations must be iterable")
    balance = 0
    for op in iterator:
        if not isinstance(op, (int, float, bool)):
            raise TypeError("operations must contain numeric values")
        balance += op
        if balance < 0:
            return True
    return False