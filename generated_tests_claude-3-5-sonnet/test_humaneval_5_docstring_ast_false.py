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
    from intersperse_function import intersperse
    assert intersperse(numbers, delimeter) == expected


def test_intersperse_empty_list():
    assert intersperse([], 42) == []


def test_intersperse_single_element():
    assert intersperse([7], 42) == [7]


def test_intersperse_same_numbers():
    assert intersperse([1, 1, 1], 1) == [1, 1, 1, 1, 1]


@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    True,
    (1, 2, 3),
    {1, 2, 3},
    {"a": 1}
])
def test_intersperse_invalid_input_type(invalid_input):
    with pytest.raises(TypeError):
        intersperse(invalid_input, 4)


def test_intersperse_invalid_delimiter_type():
    with pytest.raises(TypeError):
        _ = intersperse([1, 2, 3], "4")


def test_intersperse_large_numbers():
    assert intersperse([10**6, 10**7], 10**8) == [10**6, 10**8, 10**7]


def test_intersperse_list_with_none():
    with pytest.raises(TypeError):
        _ = intersperse([1, None, 3], 4)