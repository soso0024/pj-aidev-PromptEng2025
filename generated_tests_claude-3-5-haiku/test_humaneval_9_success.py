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

def test_rolling_max_normal_case():
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]
    assert rolling_max([3, 1, 4, 2, 5]) == [3, 3, 4, 4, 5]

def test_rolling_max_edge_cases():
    assert rolling_max([]) == []
    assert rolling_max([42]) == [42]
    assert rolling_max([-1, -2, -3]) == [-1, -1, -1]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [5, 5, 5, 5, 5]),
    ([3, 1, 4, 2, 5], [3, 3, 4, 4, 5]),
    ([], []),
    ([42], [42]),
    ([-1, -2, -3], [-1, -1, -1])
])
def test_rolling_max_parametrized(input_list, expected):
    assert rolling_max(input_list) == expected

def test_rolling_max_mixed_numbers():
    assert rolling_max([-5, 10, 0, -3, 15]) == [-5, 10, 10, 10, 15]

def test_rolling_max_type_error():
    with pytest.raises(TypeError):
        rolling_max([1, 2, '3'])

def test_rolling_max_large_numbers():
    large_list = list(range(1000))
    expected = [max(large_list[:i+1]) for i in range(len(large_list))]
    assert rolling_max(large_list) == expected