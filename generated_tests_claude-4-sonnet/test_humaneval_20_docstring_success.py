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

def test_basic_case():
    result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    assert result == (2.0, 2.2)

def test_identical_elements():
    result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    assert result == (2.0, 2.0)

def test_two_elements():
    result = find_closest_elements([1.0, 2.0])
    assert result == (1.0, 2.0)

def test_negative_numbers():
    result = find_closest_elements([-1.0, -2.0, -3.0, -1.5])
    assert result == (-1.5, -1.0)

def test_mixed_positive_negative():
    result = find_closest_elements([-1.0, 1.0, 0.5, -0.5])
    assert result == (-1.0, -0.5)

def test_all_same_numbers():
    result = find_closest_elements([5.0, 5.0, 5.0, 5.0])
    assert result == (5.0, 5.0)

def test_zero_included():
    result = find_closest_elements([0.0, 1.0, -1.0, 0.1])
    assert result == (0.0, 0.1)

def test_large_numbers():
    result = find_closest_elements([1000.0, 1001.0, 2000.0, 1000.5])
    assert result == (1000.0, 1000.5)

def test_decimal_precision():
    result = find_closest_elements([1.001, 1.002, 1.003, 1.0015])
    assert result == (1.0015, 1.002)

def test_three_elements():
    result = find_closest_elements([10.0, 20.0, 15.0])
    assert result == (10.0, 15.0)

def test_unsorted_list():
    result = find_closest_elements([5.0, 1.0, 3.0, 2.0, 4.0])
    assert result == (4.0, 5.0)

def test_very_small_differences():
    result = find_closest_elements([1.0000001, 1.0000002, 2.0])
    assert result == (1.0000001, 1.0000002)

def test_multiple_pairs_same_distance():
    result = find_closest_elements([1.0, 2.0, 3.0, 4.0])
    assert result in [(1.0, 2.0), (2.0, 3.0), (3.0, 4.0)]

def test_large_list():
    numbers = [i * 0.1 for i in range(100)]
    numbers.append(5.05)
    result = find_closest_elements(numbers)
    assert result == (5.0, 5.05)