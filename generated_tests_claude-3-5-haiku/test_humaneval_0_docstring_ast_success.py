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
from typing import List
import pytest

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers[idx+1:], start=idx+1):
            distance = abs(elem - elem2)
            if distance <= threshold:
                return True
    return False

def test_has_close_elements_basic_cases():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True

@pytest.mark.parametrize("numbers,threshold,expected", [
    ([1.0, 2.0, 3.0], 0.5, False),
    ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
    ([], 1.0, False),
    ([1.0], 1.0, False),
    ([1.0, 1.1], 0.2, True),
    ([1.0, 1.0], 0.0, True),
    ([1.0, 10.0, 100.0], 0.1, False)
])
def test_has_close_elements_parametrized(numbers, threshold, expected):
    assert has_close_elements(numbers, threshold) == expected

def test_has_close_elements_negative_numbers():
    assert has_close_elements([-1.0, -1.1, 2.0], 0.2) == True
    assert has_close_elements([-10.0, -5.0, 0.0, 5.0, 10.0], 1.0) == False

def test_has_close_elements_precision():
    assert has_close_elements([1.0, 1.000001], 0.0001) == True
    assert has_close_elements([1.0, 1.1], 0.05) == False

def test_has_close_elements_large_lists():
    large_list = list(range(1000))
    assert has_close_elements(large_list, 0.1) == False

def test_has_close_elements_zero_threshold():
    assert has_close_elements([1.0, 1.0, 2.0], 0.0) == True