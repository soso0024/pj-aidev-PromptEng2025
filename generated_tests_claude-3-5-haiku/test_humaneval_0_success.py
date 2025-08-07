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

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance <= threshold:
                    return True

    return False

def test_has_close_elements_basic_case():
    assert has_close_elements([1.0, 2.0, 3.0], 1.5) == True
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False

def test_has_close_elements_edge_cases():
    assert has_close_elements([], 1.0) == False
    assert has_close_elements([1.0], 1.0) == False

def test_has_close_elements_negative_numbers():
    assert has_close_elements([-1.0, 1.0, 2.0], 2.0) == True
    assert has_close_elements([-5.0, -4.9, 3.0], 0.2) == True

def test_has_close_elements_zero_threshold():
    assert has_close_elements([1.0, 1.0, 2.0], 0.0) == True

@pytest.mark.parametrize("numbers,threshold,expected", [
    ([1.0, 2.0, 3.0], 1.5, True),
    ([1.0, 2.0, 3.0], 0.5, False),
    ([-1.0, 1.0, 2.0], 2.0, True),
    ([], 1.0, False),
    ([1.0], 1.0, False),
    ([1.0, 1.0, 2.0], 0.0, True)
])
def test_has_close_elements_parametrized(numbers, threshold, expected):
    assert has_close_elements(numbers, threshold) == expected