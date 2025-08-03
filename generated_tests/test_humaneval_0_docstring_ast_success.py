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
import math


@pytest.mark.parametrize("numbers,threshold,expected", [
    ([1.0, 2.0, 3.0], 0.5, False),
    ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
    ([], 1.0, False),
    ([1.0], 1.0, False),
    ([1.0, 1.0], 0.1, True),
    ([1.0, 2.0, 3.0, 4.0], 0.01, False),
    ([1.0, 1.000001], 0.0001, True),
    ([1.0, 1.000001], 0.001, True),
    ([-1.0, 1.0], 1.5, False),
    ([-1.0, 1.0], 2.5, True),
    ([0.0, 0.0, 0.0], 0.1, True),
    ([float('inf'), float('inf')], 0.1, False),
    ([float('-inf'), float('inf')], 0.1, False),
])
def test_has_close_elements(numbers: List[float], threshold: float, expected: bool):
    assert has_close_elements(numbers, threshold) == expected


@pytest.mark.parametrize("invalid_input", [
    ("not a list", 1.0),
    ([1, "2", 3], 1.0),
    ([1.0, 2.0], "not a float"),
    (None, 1.0),
    ([1.0, 2.0], None),
])
def test_has_close_elements_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        has_close_elements(*invalid_input)


def test_has_close_elements_with_nan():
    numbers = [float('nan'), 1.0]
    threshold = 0.1
    result = has_close_elements(numbers, threshold)
    assert not result


@pytest.mark.parametrize("numbers,threshold", [
    ([1.0, 2.0], -1.0),
    ([1.0, 2.0], 0.0),
])
def test_has_close_elements_non_positive_threshold(numbers, threshold):
    result = has_close_elements(numbers, threshold)
    assert not result