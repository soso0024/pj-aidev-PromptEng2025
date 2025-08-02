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
    ([-1.0, 1.0], (-1.0, 1.0)),
    ([0.0, 0.1, -0.1], (-0.1, 0.0)),
    ([10.5, 10.6, 10.7, 10.8], (10.5, 10.6)),
    ([1.0, 5.0, 2.0, 8.0], (1.0, 2.0)),
    ([0.0, 0.0, 1.0], (0.0, 0.0)),
])
def test_find_closest_elements_normal_cases(numbers, expected):
    result = find_closest_elements(numbers)
    assert result == expected

@pytest.mark.parametrize("numbers", [
    [1.0],
    [],
])
def test_find_closest_elements_invalid_input(numbers):
    with pytest.raises(ValueError):
        find_closest_elements(numbers)

def test_find_closest_elements_identical_numbers():
    assert find_closest_elements([2.0, 2.0, 2.0]) == (2.0, 2.0)

def test_find_closest_elements_negative_numbers():
    assert find_closest_elements([-5.0, -4.0, -6.0, -3.0]) == (-5.0, -4.0)

def test_find_closest_elements_large_numbers():
    assert find_closest_elements([1000.0, 1000.1, 1000.2]) == (1000.0, 1000.1)

def test_find_closest_elements_mixed_numbers():
    assert find_closest_elements([-1.5, 1.5, 0.0, -0.1]) == (-0.1, 0.0)

@pytest.mark.parametrize("numbers", [
    ["1.0", "2.0"],
    [None, 1.0],
    [1, 2],
])
def test_find_closest_elements_invalid_types(numbers):
    with pytest.raises(TypeError):
        find_closest_elements(numbers)

def test_find_closest_elements_floating_point_precision():
    result = find_closest_elements([0.1 + 0.2, 0.3, 0.4])
    assert abs(result[0] - 0.3) < 1e-10
    assert abs(result[1] - 0.3) < 1e-10

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    if not all(isinstance(x, float) for x in numbers):
        raise TypeError("All elements must be floats")
        
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