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

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise TypeError("List must contain at least two elements")

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

def test_find_closest_elements_normal_case():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

def test_find_closest_elements_duplicate_values():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

def test_find_closest_elements_negative_numbers():
    assert find_closest_elements([-1.0, -2.0, 3.0, 4.0, 5.0, -1.5]) == (-1.5, -1.0)

def test_find_closest_elements_mixed_numbers():
    assert find_closest_elements([-1.0, 2.0, 3.0, 4.0, 5.0, 1.5]) == (1.5, 2.0)

@pytest.mark.parametrize("input_list,expected", [
    ([1.0, 1.1, 1.2], (1.1, 1.2)),
    ([5.5, 5.6, 5.7], (5.5, 5.6)),
    ([-10.0, -10.1, -10.2], (-10.1, -10.0))
])
def test_find_closest_elements_parametrized(input_list, expected):
    assert find_closest_elements(input_list) == expected

def test_find_closest_elements_minimum_length():
    with pytest.raises(TypeError):
        find_closest_elements([1.0])

def test_find_closest_elements_empty_list():
    with pytest.raises(TypeError):
        find_closest_elements([])