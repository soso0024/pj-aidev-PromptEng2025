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

@pytest.mark.parametrize("numbers,delimiter,expected", [
    ([], 0, []),
    ([1], 0, [1]),
    ([1, 2], 0, [1, 0, 2]),
    ([1, 2, 3], 0, [1, 0, 2, 0, 3]),
    ([-1, -2, -3], 5, [-1, 5, -2, 5, -3]),
    ([1000000, 2000000], 0, [1000000, 0, 2000000]),
    ([1, 2], "sep", [1, "sep", 2]),
    ([1, 2], None, [1, None, 2]),
    ([1, 2], [0], [1, [0], 2]),
])
def test_intersperse_basic(numbers, delimiter, expected):
    assert intersperse(numbers, delimiter) == expected

def test_original_list_unchanged():
    original = [1, 2, 3]
    copy = original.copy()
    intersperse(original, 0)
    assert original == copy

def test_returns_new_list():
    original = [1, 2, 3]
    result = intersperse(original, 0)
    assert result is not original
    assert result == [1, 0, 2, 0, 3]