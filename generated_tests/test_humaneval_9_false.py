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
from typing import List

def test_rolling_max_parametrized(numbers, expected):
    assert rolling_max(numbers) == expected

test_rolling_max_parametrized = pytest.mark.parametrize("numbers,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [3, 3, 3]),
    ([1, 1, 1], [1, 1, 1]),
    ([5, 2, 8, 1, 9], [5, 5, 8, 8, 9]),
    ([], []),
    ([42], [42]),
    ([-1, -2, -3], [-1, -1, -1]),
    ([-3, -2, -1], [-3, -2, -1]),
    ([0, 0, 0], [0, 0, 0]),
    ([10, -5, 8, -2, 15], [10, 10, 10, 10, 15]),
])(test_rolling_max_parametrized)

def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    result = []
    
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)
    return result

def test_rolling_max_single_element():
    assert rolling_max([999]) == [999]

def test_rolling_max_empty_list():
    assert rolling_max([]) == []

def test_rolling_max_negative_numbers():
    assert rolling_max([-5, -3, -7, -2]) == [-5, -3, -3, -2]

def test_rolling_max_same_numbers():
    assert rolling_max([4, 4, 4, 4]) == [4, 4, 4, 4]

def test_rolling_max_ascending():
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_rolling_max_descending():
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

def test_rolling_max_mixed_signs():
    assert rolling_max([-2, 5, -1, 8, -3]) == [-2, 5, 5, 8, 8]

def test_rolling_max_large_numbers():
    assert rolling_max([1000000, 999999, 1000001]) == [1000000, 1000000, 1000001]

def test_rolling_max_type_error():
    with pytest.raises(TypeError):
        rolling_max(None)

def test_rolling_max_invalid_input():
    with pytest.raises((TypeError, AttributeError)):
        rolling_max("not a list")