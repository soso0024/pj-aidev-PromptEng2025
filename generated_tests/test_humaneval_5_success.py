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
    ([1, 1, 1], 1, [1, 1, 1, 1, 1]),
    ([42, 42], -1, [42, -1, 42]),
    ([0], 0, [0]),
    ([999, 888, 777], 111, [999, 111, 888, 111, 777]),
    ([-1, -2, -3], 0, [-1, 0, -2, 0, -3]),
    ([0, 0, 0, 0], 99, [0, 99, 0, 99, 0, 99, 0])
])
def test_intersperse_parametrized(numbers, delimeter, expected):
    assert intersperse(numbers, delimeter) == expected

def test_intersperse_empty_list():
    assert intersperse([], 42) == []

def test_intersperse_single_element():
    assert intersperse([7], 0) == [7]

def test_intersperse_preserves_original_list():
    original = [1, 2, 3]
    original_copy = original.copy()
    intersperse(original, 0)
    assert original == original_copy

def test_intersperse_large_numbers():
    assert intersperse([1000000, 2000000], 999999) == [1000000, 999999, 2000000]

def test_intersperse_result_type():
    result = intersperse([1, 2], 3)
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)
