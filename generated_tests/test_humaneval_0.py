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


def test_has_close_elements_basic():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True


def test_has_close_elements_empty_list():
    assert has_close_elements([], 1.0) == False


def test_has_close_elements_single_element():
    assert has_close_elements([1.0], 1.0) == False


def test_has_close_elements_identical_elements():
    assert has_close_elements([1.0, 1.0], 0.1) == True


def test_has_close_elements_negative_numbers():
    assert has_close_elements([-1.0, -2.0, -3.0], 0.5) == False
    assert has_close_elements([-1.0, -1.1], 0.2) == True


def test_has_close_elements_mixed_numbers():
    assert has_close_elements([-1.0, 1.0], 1.5) == False
    assert has_close_elements([-1.0, 1.0], 2.5) == True


def test_has_close_elements_zero():
    assert has_close_elements([0.0, 0.0], 0.1) == True
    assert has_close_elements([0.0, 0.1, 0.2], 0.05) == False


def test_has_close_elements_large_numbers():
    assert has_close_elements([1000.0, 1000.1], 0.2) == True
    assert has_close_elements([1000.0, 1001.0], 0.5) == False


def test_has_close_elements_small_threshold():
    assert has_close_elements([1.0, 1.01], 0.001) == False
    assert has_close_elements([1.0, 1.001], 0.01) == True


@pytest.mark.parametrize("numbers,threshold,expected", [
