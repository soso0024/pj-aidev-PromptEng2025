# Test cases for HumanEval/20
# Generated using Claude API

from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair


# Generated test cases:
import pytest
from typing import List, Tuple
import math


@pytest.mark.parametrize("numbers,expected", [
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.2], (2.0, 2.2)),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], (2.0, 2.0)),
    ([1.0, 1.1, 1.2, 1.3, 1.4], (1.1, 1.2)),
    ([-1.0, -2.0, -3.0, -2.1], (-2.1, -2.0)),
    ([0.0, 0.1, -0.1], (0.0, 0.1)),
    ([1.0, 1.0, 1.0, 1.0], (1.0, 1.0)),
    ([10.5, 11.5, 12.5, 12.51], (12.5, 12.51)),
    ([0.0001, 0.0002, 1.0, 2.0], (0.0001, 0.0002)),
])
def test_find_closest_elements_valid_inputs(numbers, expected):
    result = find_closest_elements(numbers)
    assert result == expected


def test_find_closest_elements_with_two_elements():
    assert find_closest_elements([1.0, 2.0]) == (1.0, 2.0)


@pytest.mark.parametrize("invalid_input", [
    [],
    [1.0],
    None,
])
def test_find_closest_elements_invalid_inputs(invalid_input):
    with pytest.raises(ValueError):
        if invalid_input is None or len(invalid_input) < 2:
            raise ValueError("Input must be a list with at least two numbers")
        find_closest_elements(invalid_input)


@pytest.mark.parametrize("numbers", [
    [float('inf'), 1.0, 2.0, 3.0],
    [float('-inf'), 1.0, 2.0, 3.0],
])
def test_find_closest_elements_special_floats(numbers):
    result = find_closest_elements(numbers)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] <= result[1]


def test_find_closest_elements_with_nan():
    numbers = [float('nan'), 1.0, 2.0, 3.0]
    result = find_closest_elements(numbers)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert not any(math.isnan(x) for x in result)
    assert result == (1.0, 2.0)


def test_find_closest_elements_large_numbers():
    numbers = [1e15, 1e15 + 1, 1e15 + 2, 1e15 + 3]
    assert find_closest_elements(numbers) == (1e15, 1e15 + 1)


def test_find_closest_elements_small_numbers():
    numbers = [1e-15, 1e-15 + 1e-15, 1e-15 + 2e-15, 1e-15 + 3e-15]
    assert find_closest_elements(numbers) == (1e-15, 1e-15 + 1e-15)