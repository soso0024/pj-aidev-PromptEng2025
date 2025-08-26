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
from typing import List

def test_find_closest_elements_normal_case():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = find_closest_elements(numbers)
    assert result == (1.0, 2.0)

def test_find_closest_elements_negative_numbers():
    numbers = [-5.0, -3.0, -1.0, 0.0, 2.0]
    result = find_closest_elements(numbers)
    assert result == (-1.0, 0.0)

def test_find_closest_elements_mixed_numbers():
    numbers = [-2.5, 0.0, 1.5, 3.7, 4.2]
    result = find_closest_elements(numbers)
    assert result == (3.7, 4.2)

def test_find_closest_elements_duplicate_numbers():
    numbers = [1.0, 1.0, 2.0, 2.0, 3.0]
    result = find_closest_elements(numbers)
    assert result == (1.0, 1.0)

def test_find_closest_elements_single_element():
    numbers = [42.0]
    result = find_closest_elements(numbers)
    assert result is None

def test_find_closest_elements_empty_list():
    numbers = []
    result = find_closest_elements(numbers)
    assert result is None

@pytest.mark.parametrize("input_numbers,expected", [
    ([1.0, 2.0, 3.0], (1.0, 2.0)),
    ([-1.0, 0.0, 1.0], (-1.0, 0.0)),
    ([0.5, 1.5, 2.5], (0.5, 1.5)),
])
def test_find_closest_elements_parametrized(input_numbers, expected):
    result = find_closest_elements(input_numbers)
    assert result == expected
