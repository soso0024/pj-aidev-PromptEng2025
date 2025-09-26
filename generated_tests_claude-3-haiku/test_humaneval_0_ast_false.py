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

@pytest.mark.parametrize("numbers, threshold, expected", [
    ([1.0, 2.0, 3.0], 0.5, True),
    ([1.0, 2.0, 3.0], 1.0, True),
    ([1.0, 2.0, 3.0], 1.1, False),
    ([1.0, 1.0, 1.0], 0.1, True),
    ([1.0, 1.0, 1.0], 0.0, True),
    ([], 0.5, False),
    ([1.0], 0.5, False),
    ([1.0, 2.0], 0.5, True),
    ([1.0, 2.0], 0.9, False),
    ([-1.0, 1.0, 0.0], 1.0, True),
    ([-1.0, 1.0, 0.0], 0.5, False),
    ([float('inf'), float('inf'), float('inf')], 0.0, True),
    ([float('inf'), float('inf'), float('inf')], 0.1, True),
    ([float('nan'), float('nan'), float('nan')], 0.0, False),
])
def test_has_close_elements(numbers, threshold, expected):
    assert has_close_elements(numbers, threshold) == expected

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i, elem in enumerate(numbers):
        for j, elem2 in enumerate(numbers):
            if i != j:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False