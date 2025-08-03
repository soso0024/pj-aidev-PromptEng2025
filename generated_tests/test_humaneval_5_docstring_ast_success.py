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
    ([], 4, []),
    ([1], 4, [1]),
    ([1, 2], 4, [1, 4, 2]),
    ([1, 2, 3], 4, [1, 4, 2, 4, 3]),
    ([0, 0, 0], 1, [0, 1, 0, 1, 0]),
    ([-1, -2, -3], 0, [-1, 0, -2, 0, -3]),
    ([999], 888, [999]),
    ([1, 2, 3, 4, 5], 0, [1, 0, 2, 0, 3, 0, 4, 0, 5]),
])
def test_intersperse_valid_inputs(numbers, delimeter, expected):
    assert intersperse(numbers, delimeter) == expected


def test_intersperse_empty_list():
    assert intersperse([], 42) == []


def test_intersperse_single_element():
    assert intersperse([7], 42) == [7]


@pytest.mark.parametrize("numbers, delimeter", [
    (None, 4),
    ("not_a_list", 4),
    ([1, 2, "3"], 4),
    ([1, 2, 3], "4"),
    ([1.5, 2.5], 4),
])
def test_intersperse_invalid_inputs(numbers, delimeter):
    with pytest.raises(TypeError):
        intersperse(numbers, delimeter)


def test_intersperse_large_list():
    input_list = list(range(1000))
    result = intersperse(input_list, -1)
    assert len(result) == 1999
    assert all(result[i] == input_list[i//2] for i in range(0, len(result), 2))
    assert all(x == -1 for x in result[1::2])
    assert result[-1] == input_list[-1]


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements must be integers")
    if not isinstance(delimeter, int):
        raise TypeError("Delimiter must be an integer")

    if not numbers:
        return []

    result = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)
    result.append(numbers[-1])
    return result