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

def test_rolling_max_normal_sequence():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]

def test_rolling_max_single_element():
    assert rolling_max([5]) == [5]

def test_rolling_max_empty_list():
    assert rolling_max([]) == []

def test_rolling_max_descending_sequence():
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

def test_rolling_max_ascending_sequence():
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_rolling_max_repeated_elements():
    assert rolling_max([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]

def test_rolling_max_mixed_positive_negative():
    assert rolling_max([-1, 5, -3, 7, 2]) == [-1, 5, 5, 7, 7]

def test_rolling_max_all_negative():
    assert rolling_max([-5, -4, -3, -2, -1]) == [-5, -4, -3, -2, -1]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 2, 3, 4, 2], [1, 2, 3, 3, 3, 4, 4]),
    ([5], [5]),
    ([], []),
    ([5, 4, 3, 2, 1], [5, 5, 5, 5, 5]),
    ([-1, 5, -3, 7, 2], [-1, 5, 5, 7, 7])
])
def test_rolling_max_parametrized(input_list, expected):
    assert rolling_max(input_list) == expected
