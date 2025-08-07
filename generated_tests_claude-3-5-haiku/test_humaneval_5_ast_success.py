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
    assert intersperse([], 0) == []

def test_intersperse_single_element():
    assert intersperse([5], 0) == [5]

@pytest.mark.parametrize("numbers,delimeter,expected", [
    ([1, 2, 3], 0, [1, 0, 2, 0, 3]),
    ([10, 20], 5, [10, 5, 20]),
    ([-1, -2, -3], 100, [-1, 100, -2, 100, -3]),
    ([0], 7, [0])
])
def test_intersperse_multiple_cases(numbers, delimeter, expected):
    assert intersperse(numbers, delimeter) == expected

def test_intersperse_large_numbers():
    assert intersperse([1000000, 2000000], 500000) == [1000000, 500000, 2000000]

def test_intersperse_negative_delimiter():
    assert intersperse([1, 2, 3], -5) == [1, -5, 2, -5, 3]
