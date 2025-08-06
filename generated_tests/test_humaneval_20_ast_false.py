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

@pytest.mark.parametrize("numbers,expected", [
    ([1.0, 2.0, 3.0, 4.0], (1.0, 2.0)),
    ([1.0, 1.1, 1.2, 1.3], (1.0, 1.1)),
    ([0.0, 5.0, 2.5, 2.6], (2.5, 2.6)),
    ([1.5, 1.5, 1.5, 1.6], (1.5, 1.5)),
    ([-1.0, 1.0, -2.0, 2.0], (-2.0, -1.0)),
    ([0.1, 0.2, 0.3, 0.4], (0.1, 0.2)),
    ([10.5, 10.6, 10.7, 10.8], (10.5, 10.6)),
    ([-5.5, -5.6, -5.7, -5.8], (-5.6, -5.5)),
])
def test_find_closest_elements_normal_cases(numbers, expected):
    result = find_closest_elements(numbers)
    assert result == expected

@pytest.mark.parametrize("numbers", [
    [1.0, 2.0],
    [0.0, 1.0],
    [-1.0, 1.0],
    [0.5, 0.6],
])
def test_find_closest_elements_two_numbers(numbers):
    result = find_closest_elements(numbers)
    assert result == tuple(sorted(numbers))

def test_find_closest_elements_identical_numbers():
    numbers = [2.0, 2.0, 2.0, 2.0]
    result = find_closest_elements(numbers)
    assert result == (2.0, 2.0)

def test_find_closest_elements_negative_numbers():
    numbers = [-5.0, -4.0, -3.0, -2.0]
    result = find_closest_elements(numbers)
    assert result == (-5.0, -4.0)

@pytest.mark.parametrize("invalid_input", [
    [],
    [1.0],
])
def test_find_closest_elements_invalid_input(invalid_input):
    with pytest.raises(ValueError):
        find_closest_elements(invalid_input)

def test_find_closest_elements_large_numbers():
    numbers = [1000000.0, 1000001.0, 1000002.0, 1000003.0]
    result = find_closest_elements(numbers)
    assert result == (1000000.0, 1000001.0)

def test_find_closest_elements_small_differences():
    numbers = [0.0001, 0.0002, 0.0003, 0.0004]
    result = find_closest_elements(numbers)
    assert result == (0.0001, 0.0002)

def test_find_closest_elements_mixed_numbers():
    numbers = [-1.5, 2.5, 0.0, 1.0]
    result = find_closest_elements(numbers)
    assert result == (0.0, 1.0)

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")

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