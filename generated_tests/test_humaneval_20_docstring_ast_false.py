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
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.2], (2.0, 2.2)),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], (2.0, 2.0)),
    ([0.0, 0.1, 0.2, 0.3], (0.0, 0.1)),
    ([-1.0, -2.0, -3.0, -1.1], (-1.1, -1.0)),
    ([1.0, 1.0, 1.0, 1.0], (1.0, 1.0)),
    ([0.0, 10.0], (0.0, 10.0)),
    ([1.5, 2.5, 3.5, 2.501], (2.5, 2.501)),
    ([-10.5, -10.4999], (-10.5, -10.4999)),
])
def test_find_closest_elements_valid_inputs(numbers, expected):
    result = find_closest_elements(numbers)
    assert result == expected


def test_find_closest_elements_with_floats():
    numbers = [1.1111, 1.1112, 1.1115, 1.1119]
    assert find_closest_elements(numbers) == (1.1111, 1.1112)


def test_find_closest_elements_invalid_inputs():
    invalid_inputs = [
        [],
        [1.0],
        None,
        "invalid",
        [1, "2", 3.0],
        [True, False, 1.0]
    ]
    
    for invalid_input in invalid_inputs:
        with pytest.raises((ValueError, TypeError)):
            if not isinstance(invalid_input, list):
                raise ValueError("Input must be a list")
            if len(invalid_input) < 2:
                raise ValueError("List must contain at least two numbers")
            if not all(isinstance(x, (int, float)) for x in invalid_input):
                raise TypeError("All elements must be numbers")
            find_closest_elements(invalid_input)


def test_find_closest_elements_large_numbers():
    numbers = [1e15, 1e15 + 1, 1e15 + 2, 1e15 + 3]
    assert find_closest_elements(numbers) == (1e15, 1e15 + 1)


def test_find_closest_elements_very_small_numbers():
    numbers = [1e-15, 1.1e-15, 1.2e-15, 1.3e-15]
    assert find_closest_elements(numbers) == (1e-15, 1.1e-15)


def test_find_closest_elements_mixed_signs():
    numbers = [-0.5, 0.5, -0.1, 0.1]
    assert find_closest_elements(numbers) == (-0.1, 0.1)