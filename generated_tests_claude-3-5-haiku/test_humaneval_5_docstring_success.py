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

def test_empty_list():
    assert intersperse([], 4) == []

def test_single_element_list():
    assert intersperse([1], 4) == [1]

def test_multiple_elements():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

def test_negative_delimiter():
    assert intersperse([1, 2, 3], -4) == [1, -4, 2, -4, 3]

def test_zero_delimiter():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

@pytest.mark.parametrize("input_list,delimiter,expected", [
    ([], 4, []),
    ([1], 4, [1]),
    ([1, 2, 3], 4, [1, 4, 2, 4, 3]),
    ([10, 20, 30, 40], 5, [10, 5, 20, 5, 30, 5, 40]),
    ([-1, -2, -3], 0, [-1, 0, -2, 0, -3])
])
def test_intersperse_parametrized(input_list, delimiter, expected):
    assert intersperse(input_list, delimiter) == expected
