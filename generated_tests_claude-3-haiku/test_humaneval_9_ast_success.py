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
    assert rolling_max([]) == []

def test_rolling_max_single_element():
    assert rolling_max([5]) == [5]

def test_rolling_max_increasing_sequence():
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_rolling_max_decreasing_sequence():
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

def test_rolling_max_mixed_sequence():
    assert rolling_max([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [3, 3, 4, 4, 5, 9, 9, 9, 9]

def test_rolling_max_duplicate_elements():
    assert rolling_max([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [5, 5, 5, 5, 5]),
    ([], []),
    ([1], [1]),
    ([3, 1, 4, 1, 5, 9, 2, 6, 5], [3, 3, 4, 4, 5, 9, 9, 9, 9])
])
def test_rolling_max_parametrized(input, expected):
    assert rolling_max(input) == expected

def test_rolling_max_none_input():
    with pytest.raises(TypeError):
        rolling_max(None)

def test_rolling_max_non_integer_input():
    with pytest.raises(TypeError):
        rolling_max([1, 2, 'a', 4])
