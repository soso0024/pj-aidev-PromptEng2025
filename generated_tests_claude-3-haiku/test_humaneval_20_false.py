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

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair = None
    distance = None

    if len(numbers) < 2:
        return (None, None)

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                new_distance = abs(elem - elem2)
                if distance is None or new_distance < distance:
                    distance = new_distance
                    closest_pair = tuple(sorted([elem, elem2]))

    if closest_pair is None:
        return (None, None)
    else:
        return closest_pair

def test_find_closest_elements_empty_list():
    assert find_closest_elements([]) == (None, None)

def test_find_closest_elements_single_element():
    assert find_closest_elements([1.0]) == (1.0, 1.0)

def test_find_closest_elements_two_elements():
    assert find_closest_elements([1.0, 2.0]) == (1.0, 2.0)
    assert find_closest_elements([2.0, 1.0]) == (1.0, 2.0)

def test_find_closest_elements_multiple_elements():
    assert find_closest_elements([1.0, 2.0, 3.0]) == (1.0, 2.0)
    assert find_closest_elements([3.0, 1.0, 2.0]) == (1.0, 2.0)
    assert find_closest_elements([1.0, 1.5, 2.0]) == (1.0, 1.5)
    assert find_closest_elements([1.0, 1.1, 1.2]) == (1.0, 1.1)

def test_find_closest_elements_negative_numbers():
    assert find_closest_elements([-1.0, -2.0, -3.0]) == (-3.0, -2.0)
    assert find_closest_elements([-1.0, -1.5, -2.0]) == (-2.0, -1.5)

def test_find_closest_elements_mixed_numbers():
    assert find_closest_elements([-1.0, 1.0, 2.0]) == (-1.0, 1.0)
    assert find_closest_elements([-1.0, 0.0, 1.0]) == (-1.0, 0.0)

def test_find_closest_elements_duplicate_numbers():
    assert find_closest_elements([1.0, 1.0, 2.0]) == (1.0, 1.0)
    assert find_closest_elements([1.0, 1.0, 1.0]) == (1.0, 1.0)