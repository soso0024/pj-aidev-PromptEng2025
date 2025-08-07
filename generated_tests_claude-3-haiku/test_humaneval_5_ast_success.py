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

@pytest.mark.parametrize("numbers,delimeter,expected", [
    ([1, 2, 3], 0, [1, 0, 2, 0, 3]),
    ([10, 20, 30, 40], 5, [10, 5, 20, 5, 30, 5, 40]),
    ([100], 1, [100]),
    ([1, 2, 3, 4, 5], 99, [1, 99, 2, 99, 3, 99, 4, 99, 5])
])
def test_intersperse_normal_cases(numbers, delimeter, expected):
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
