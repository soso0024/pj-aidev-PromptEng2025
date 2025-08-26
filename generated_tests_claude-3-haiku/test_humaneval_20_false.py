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
from typing import List, Tuple
import pytest

def test_find_closest_elements_empty_list():
    assert find_closest_elements([]) is None

def test_find_closest_elements_single_element():
    assert find_closest_elements([1.0]) is None

def test_find_closest_elements_two_elements():
    assert find_closest_elements([1.0, 2.0]) == (1.0, 2.0)

def test_find_closest_elements_multiple_elements():
    assert find_closest_elements([1.0, 2.0, 2.5, 3.0]) == (2.0, 2.5)

def test_find_closest_elements_negative_numbers():
    assert find_closest_elements([-2.0, -1.0, 1.0, 2.0]) == (-1.0, 1.0)

def test_find_closest_elements_duplicate_elements():
    assert find_closest_elements([1.0, 1.0, 2.0, 2.0]) == (1.0, 1.0)

@pytest.mark.parametrize("input,expected", [
    ([1.0, 2.0, 3.0, 4.0], (1.0, 2.0)),
    ([10.0, 10.1, 10.2, 10.3], (10.0, 10.1)),
    ([-5.0, -4.5, -4.0, -3.5], (-4.5, -4.0)),
    ([0.0, 0.1, 0.2, 0.3], (0.0, 0.1)),
])
def test_find_closest_elements_parametrized(input, expected):
    assert find_closest_elements(input) == expected