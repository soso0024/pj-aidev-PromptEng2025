# Test cases for HumanEval/0
# Generated using Claude API

from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False


# Generated test cases:
import pytest
from solution import has_close_elements

def test_close_elements_detected():
    numbers = [1.0, 2.5, 3.0, 4.5]
    threshold = 1.6
    assert has_close_elements(numbers, threshold) is True

def test_no_close_elements():
    numbers = [1.0, 3.5, 6.0, 9.5]
    threshold = 1.0
    assert has_close_elements(numbers, threshold) is False

def test_empty_list():
    assert has_close_elements([], 1.0) is False

def test_single_element():
    assert has_close_elements([5.0], 1.0) is False

def test_threshold_zero_no_duplicates():
    numbers = [1.0, 2.0, 3.0]
    assert has_close_elements(numbers, 0.0) is False

def test_threshold_zero_with_duplicates():
    numbers = [1.0, 1.0, 2.0]
    assert has_close_elements(numbers, 0.0) is False

def test_negative_threshold():
    numbers = [1.0, 2.0, 3.0]
    assert has_close_elements(numbers, -1.0) is False

def test_close_elements_with_negative_numbers():
    numbers = [-5.0, -4.5, -3.0]
    threshold = 0.6
    assert has_close_elements(numbers, threshold) is True

def test_close_elements_at_threshold_boundary():
    numbers = [0.0, 1.0, 2.0]
    threshold = 1.0
    assert has_close_elements(numbers, threshold) is False

def test_multiple_close_pairs():
    numbers = [0.0, 0.5, 1.0, 1.5]
    threshold = 0.6
    assert has_close_elements(numbers, threshold) is True