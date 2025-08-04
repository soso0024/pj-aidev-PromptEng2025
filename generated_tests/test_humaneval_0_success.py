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
    ([1.0, 2.0, 3.0, 4.0], 0.5, False),
    ([1.0, 2.0, 3.0, 4.0], 1.5, True),
    ([1.0, 2.0, 3.0, 4.0], 1.0, False),
    ([], 1.0, False),
    ([1.0], 1.0, False),
    ([1.0, 1.0], 0.5, True),
    ([1.0, 1.001], 0.01, True),
    ([1.0, 2.0], 0.1, False),
    ([-1.0, 1.0], 1.5, False),
    ([-1.0, -1.5, -2.0], 0.4, False),
    ([10.0, 20.0, 30.0, 40.0], 5.0, False),
    ([0.1, 0.2, 0.3, 0.4], 0.05, False),
    ([1.0, 1.0, 1.0], 0.0001, True),
    ([1.0, 2.0, float("inf")], 1.0, False),
    ([-float("inf"), 1.0, float("inf")], 2.0, False)
])
def test_has_close_elements(numbers: List[float], threshold: float, expected: bool):
    assert has_close_elements(numbers, threshold) == expected

@pytest.mark.parametrize("invalid_input", [
    ("not_a_list", 1.0),
    ([1, 2, "3"], 1.0),
    ([1.0, 2.0], "not_a_float"),
    (None, 1.0),
    ([1.0, 2.0], None)
])
def test_has_close_elements_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        has_close_elements(*invalid_input)

def test_has_close_elements_negative_threshold():
    result = has_close_elements([1.0, 2.0], -1.0)
    assert result == False

def test_has_close_elements_zero_threshold():
    assert has_close_elements([1.0, 1.0], 0.0) == False
    assert has_close_elements([1.0, 1.1], 0.0) == False

def test_has_close_elements_nan():
    assert has_close_elements([1.0, float('nan')], 1.0) == False
    assert has_close_elements([float('nan'), float('nan')], 1.0) == False