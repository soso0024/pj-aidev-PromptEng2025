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

def test_intersperse_multiple_elements():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

def test_intersperse_negative_delimiter():
    assert intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

def test_intersperse_large_numbers():
    assert intersperse([1000, 2000, 3000], 500) == [1000, 500, 2000, 500, 3000]

@pytest.mark.parametrize("numbers,delimiter,expected", [
    ([], 0, []),
    ([5], 0, [5]),
    ([1, 2, 3], 0, [1, 0, 2, 0, 3]),
    ([1, 2, 3], -1, [1, -1, 2, -1, 3]),
    ([1000, 2000, 3000], 500, [1000, 500, 2000, 500, 3000])
])
def test_intersperse_parametrized(numbers, delimiter, expected):
    assert intersperse(numbers, delimiter) == expected
