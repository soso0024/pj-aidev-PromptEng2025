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
def test_intersperse_parametrized(numbers, delimeter, expected):
    assert intersperse(numbers, delimeter) == expected


def test_intersperse_empty_list():
    assert intersperse([], 42) == []


def test_intersperse_single_element():
    assert intersperse([7], 42) == [7]


def test_intersperse_preserves_order():
    input_list = [1, 2, 3, 4]
    result = intersperse(input_list, 0)
    assert result[::2] == input_list


def test_intersperse_delimeter_appears_correct_times():
    result = intersperse([1, 2, 3, 4], 42)
    assert result.count(42) == 3


def test_intersperse_type_preservation():
    result = intersperse([1, 2, 3], 4)
    assert all(isinstance(x, int) for x in result)


@pytest.mark.parametrize("invalid_input", [
    123,
    True,
    3.14
])
def test_intersperse_invalid_input_type(invalid_input):
    with pytest.raises(TypeError):
        intersperse(invalid_input, 4)


def test_intersperse_large_list():
    large_list = list(range(1000))
    result = intersperse(large_list, -1)
    assert len(result) == 1999
    assert result[::2] == large_list