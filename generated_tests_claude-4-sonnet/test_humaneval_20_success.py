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

def find_closest_elements(numbers: List[float]):
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

def test_empty_list():
    assert find_closest_elements([]) is None

def test_single_element():
    assert find_closest_elements([5.0]) is None

def test_two_elements():
    result = find_closest_elements([1.0, 3.0])
    assert result == (1.0, 3.0)

def test_two_elements_reverse_order():
    result = find_closest_elements([3.0, 1.0])
    assert result == (1.0, 3.0)

def test_three_elements_first_two_closest():
    result = find_closest_elements([1.0, 2.0, 10.0])
    assert result == (1.0, 2.0)

def test_three_elements_last_two_closest():
    result = find_closest_elements([1.0, 10.0, 11.0])
    assert result == (10.0, 11.0)

def test_identical_elements():
    result = find_closest_elements([5.0, 5.0])
    assert result == (5.0, 5.0)

def test_multiple_identical_elements():
    result = find_closest_elements([3.0, 3.0, 3.0])
    assert result == (3.0, 3.0)

def test_negative_numbers():
    result = find_closest_elements([-5.0, -2.0, -1.0])
    assert result == (-2.0, -1.0)

def test_mixed_positive_negative():
    result = find_closest_elements([-1.0, 0.0, 1.0])
    assert result == (-1.0, 0.0) or result == (0.0, 1.0)

def test_floating_point_precision():
    result = find_closest_elements([1.1, 1.2, 1.3])
    assert result == (1.1, 1.2)

def test_large_numbers():
    result = find_closest_elements([1000000.0, 1000001.0, 2000000.0])
    assert result == (1000000.0, 1000001.0)

def test_very_small_differences():
    result = find_closest_elements([0.001, 0.002, 0.1])
    assert result == (0.001, 0.002)

def test_zero_included():
    result = find_closest_elements([0.0, 1.0, 2.0])
    assert result == (0.0, 1.0)

def test_all_same_distance():
    result = find_closest_elements([0.0, 1.0, 2.0, 3.0])
    assert result == (0.0, 1.0)

def test_longer_list():
    result = find_closest_elements([10.0, 5.0, 3.0, 8.0, 2.0, 15.0])
    assert result == (2.0, 3.0)

@pytest.mark.parametrize("numbers,expected", [
    ([1.0, 2.0], (1.0, 2.0)),
    ([2.0, 1.0], (1.0, 2.0)),
    ([1.0, 3.0, 2.0], (1.0, 2.0)),
    ([0.0, 0.5, 1.0], (0.0, 0.5)),
    ([-1.0, -0.5, 0.0], (-1.0, -0.5))
])
def test_parametrized_cases(numbers, expected):
    assert find_closest_elements(numbers) == expected
