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


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result


def test_intersperse_empty_list():
    assert intersperse([], 4) == []


def test_intersperse_single_element():
    assert intersperse([1], 4) == [1]


def test_intersperse_two_elements():
    assert intersperse([1, 2], 4) == [1, 4, 2]


def test_intersperse_three_elements():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]


def test_intersperse_multiple_elements():
    assert intersperse([1, 2, 3, 4, 5], 0) == [1, 0, 2, 0, 3, 0, 4, 0, 5]


def test_intersperse_negative_numbers():
    assert intersperse([-1, -2, -3], -4) == [-1, -4, -2, -4, -3]


def test_intersperse_mixed_positive_negative():
    assert intersperse([-1, 2, -3], 0) == [-1, 0, 2, 0, -3]


def test_intersperse_zero_delimiter():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]


def test_intersperse_zero_in_list():
    assert intersperse([0, 1, 0], 5) == [0, 5, 1, 5, 0]


def test_intersperse_same_numbers():
    assert intersperse([1, 1, 1], 1) == [1, 1, 1, 1, 1]


def test_intersperse_large_numbers():
    assert intersperse([1000000, 2000000], 999999) == [1000000, 999999, 2000000]


@pytest.mark.parametrize("numbers,delimiter,expected", [
    ([], 1, []),
    ([5], 9, [5]),
    ([1, 2], 3, [1, 3, 2]),
    ([10, 20, 30, 40], 99, [10, 99, 20, 99, 30, 99, 40]),
    ([0], 0, [0]),
    ([-5, -10], -1, [-5, -1, -10])
])
def test_intersperse_parametrized(numbers, delimiter, expected):
    assert intersperse(numbers, delimiter) == expected
