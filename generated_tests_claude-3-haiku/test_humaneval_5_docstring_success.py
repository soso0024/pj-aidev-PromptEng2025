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

def test_intersperse_single_element_list():
    assert intersperse([1], 4) == [1]

def test_intersperse_multiple_elements():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

@pytest.mark.parametrize("numbers,delimeter,expected", [
    ([], 0, []),
    ([1], 0, [1]),
    ([1, 2, 3], 0, [1, 0, 2, 0, 3]),
    ([1, 2, 3], -1, [1, -1, 2, -1, 3]),
    ([1, 2, 3, 4, 5], 3, [1, 3, 2, 3, 3, 3, 4, 3, 5])
])
def test_intersperse_with_different_inputs(numbers, delimeter, expected):
    assert intersperse(numbers, delimeter) == expected

def test_intersperse_with_negative_numbers():
    assert intersperse([-1, -2, -3], 4) == [-1, 4, -2, 4, -3]

def test_intersperse_with_zero_delimeter():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
