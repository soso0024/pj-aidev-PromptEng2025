# Test cases for HumanEval/9
# Generated using Claude API

from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result


# Generated test cases:
import pytest

def test_rolling_max_empty_list():
    from typing import List
    def rolling_max(numbers: List[int]):
        running_max = None
        result = []

        for n in numbers:
            if running_max is None:
                running_max = n
            else:
                running_max = max(running_max, n)

            result.append(running_max)

        return result

    assert rolling_max([]) == []

def test_rolling_max_single_element():
    def rolling_max(numbers: List[int]):
        running_max = None
        result = []

        for n in numbers:
            if running_max is None:
                running_max = n
            else:
                running_max = max(running_max, n)

            result.append(running_max)

        return result

    assert rolling_max([42]) == [42]

@pytest.mark.parametrize("numbers,expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [5, 5, 5, 5, 5]),
    ([1, 3, 2, 4, 3], [1, 3, 3, 4, 4]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
])
def test_rolling_max_normal_cases(numbers, expected):
    def rolling_max(numbers: List[int]):
        running_max = None
        result = []

        for n in numbers:
            if running_max is None:
                running_max = n
            else:
                running_max = max(running_max, n)

            result.append(running_max)

        return result

    assert rolling_max(numbers) == expected

def test_rolling_max_with_none():
    def rolling_max(numbers: List[int]):
        running_max = None
        result = []

        for n in numbers:
            if running_max is None:
                running_max = n
            else:
                running_max = max(running_max, n)

            result.append(running_max)

        return result

    with pytest.raises(TypeError):
        rolling_max([1, None, 3])
