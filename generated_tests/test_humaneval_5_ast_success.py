# Test cases for HumanEval/5
# Generated using Claude API

from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result


# Generated test cases:
import pytest
from typing import List

@pytest.mark.parametrize("numbers, delimeter, expected", [
    ([1, 2, 3], 0, [1, 0, 2, 0, 3]),
    ([1], 9, [1]),
    ([], 5, []),
    ([1, 1], 2, [1, 2, 1]),
    ([10, 20, 30, 40], -1, [10, -1, 20, -1, 30, -1, 40]),
    ([0], 0, [0]),
    ([999, 999], 999, [999, 999, 999]),
    ([-1, -2, -3], 0, [-1, 0, -2, 0, -3]),
    ([0, 0, 0], 1, [0, 1, 0, 1, 0])
])
def test_intersperse_parametrized(numbers: List[int], delimeter: int, expected: List[int]):
    assert intersperse(numbers, delimeter) == expected

def test_intersperse_empty_list():
    assert intersperse([], 42) == []

def test_intersperse_single_element():
    assert intersperse([7], 3) == [7]

def test_intersperse_two_elements():
    assert intersperse([1, 2], 0) == [1, 0, 2]

def test_intersperse_same_numbers():
    assert intersperse([5, 5, 5], 5) == [5, 5, 5, 5, 5]

def test_intersperse_negative_numbers():
    assert intersperse([-1, -2], -3) == [-1, -3, -2]

def test_intersperse_zero_delimeter():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

def test_intersperse_large_numbers():
    assert intersperse([1000000, 2000000], 999999) == [1000000, 999999, 2000000]
