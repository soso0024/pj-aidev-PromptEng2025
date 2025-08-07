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

def test_intersperse_empty_list():
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

    assert intersperse([], 5) == []

def test_intersperse_single_element_list():
    def intersperse(numbers: List[int], delimeter: int) -> List[int]:
        if not numbers:
            return []

        result = []

        for n in numbers[:-1]:
            result.append(n)
            result.append(delimeter)

        result.append(numbers[-1])

        return result

    assert intersperse([42], 5) == [42]

def test_intersperse_multiple_elements():
    def intersperse(numbers: List[int], delimeter: int) -> List[int]:
        if not numbers:
            return []

        result = []

        for n in numbers[:-1]:
            result.append(n)
            result.append(delimeter)

        result.append(numbers[-1])

        return result

    assert intersperse([1, 2, 3, 4, 5], 0) == [1, 0, 2, 0, 3, 0, 4, 0, 5]

@pytest.mark.parametrize("numbers,delimeter,expected", [
    ([], 5, []),
    ([42], 5, [42]),
    ([1, 2, 3, 4, 5], 0, [1, 0, 2, 0, 3, 0, 4, 0, 5]),
    ([10, 20, 30, 40, 50], 99, [10, 99, 20, 99, 30, 99, 40, 99, 50]),
    ([100, 200, 300], -1, [100, -1, 200, -1, 300])
])
def test_intersperse_parametrized(numbers, delimeter, expected):
    def intersperse(numbers: List[int], delimeter: int) -> List[int]:
        if not numbers:
            return []

        result = []

        for n in numbers[:-1]:
            result.append(n)
            result.append(delimeter)

        result.append(numbers[-1])

        return result

    assert intersperse(numbers, delimeter) == expected
