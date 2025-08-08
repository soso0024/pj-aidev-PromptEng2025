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
    ([999, 999], 888, [999, 888, 999]),
    ([1, 2, 3, 4, 5], 0, [1, 0, 2, 0, 3, 0, 4, 0, 5])
])
def test_intersperse_parametrized(numbers, delimeter, expected):
    from intersperse_function import intersperse
    assert intersperse(numbers, delimeter) == expected


def test_intersperse_empty_list():
    assert intersperse([], 42) == []


def test_intersperse_single_element():
    assert intersperse([7], 42) == [7]


def test_intersperse_preserves_input_types():
    result = intersperse([1, 2, 3], 0)
    assert all(isinstance(x, int) for x in result)


def test_intersperse_large_numbers():
    result = intersperse([10**6, 10**6], 10**6)
    assert result == [10**6, 10**6, 10**6]


@pytest.mark.parametrize("invalid_input", [
    123,
    True
])
def test_intersperse_invalid_input_type(invalid_input):
    with pytest.raises(TypeError):
        intersperse(invalid_input, 4)


def test_intersperse_result_length():
    input_list = [1, 2, 3, 4]
    result = intersperse(input_list, 0)
    assert len(result) == 2 * len(input_list) - 1