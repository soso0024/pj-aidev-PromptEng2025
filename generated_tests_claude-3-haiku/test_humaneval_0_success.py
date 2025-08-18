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
from typing import List

def has_close_elements(numbers: List[float], threshold: float):
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False

def test_has_close_elements_normal_case():
    assert has_close_elements([1.0, 2.0, 3.0], 1.5) is True
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) is False

def test_has_close_elements_empty_list():
    assert has_close_elements([], 1.0) is False

def test_has_close_elements_single_element_list():
    assert has_close_elements([1.0], 1.0) is False

def test_has_close_elements_all_elements_close():
    assert has_close_elements([1.0, 1.1, 1.2], 0.2) is True

def test_has_close_elements_threshold_zero():
    assert has_close_elements([1.0, 2.0, 3.0], 0.0) is False

def test_has_close_elements_negative_threshold():
    assert has_close_elements([1.0, 2.0, 3.0], -0.5) is False

def test_has_close_elements_duplicate_elements():
    assert has_close_elements([1.0, 1.0, 2.0], 0.5) is True
