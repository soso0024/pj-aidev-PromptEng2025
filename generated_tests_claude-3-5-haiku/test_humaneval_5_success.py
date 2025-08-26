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

def intersperse(numbers: List[int], delimeter: int):
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result

def test_intersperse_normal_case():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

def test_intersperse_single_element():
    assert intersperse([42], 0) == [42]

def test_intersperse_empty_list():
    assert intersperse([], 5) == []

def test_intersperse_negative_numbers():
    assert intersperse([-1, -2, -3], -10) == [-1, -10, -2, -10, -3]

def test_intersperse_mixed_numbers():
    assert intersperse([-1, 0, 1], 100) == [-1, 100, 0, 100, 1]

@pytest.mark.parametrize("input_list,delimiter,expected", [
    ([1, 2, 3], 0, [1, 0, 2, 0, 3]),
    ([42], 7, [42]),
    ([], 5, []),
    ([-1, -2, -3], -10, [-1, -10, -2, -10, -3]),
    ([0, 0, 0], 1, [0, 1, 0, 1, 0])
])
def test_intersperse_parametrized(input_list, delimiter, expected):
    assert intersperse(input_list, delimiter) == expected
