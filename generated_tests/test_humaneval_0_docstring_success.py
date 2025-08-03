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


@pytest.mark.parametrize("numbers,threshold,expected", [
    ([1.0, 2.0, 3.0], 0.5, False),
    ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
    ([], 1.0, False),
    ([1.0], 1.0, False),
    ([1.0, 1.0], 0.1, True),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 0.1, False),
    ([1.0, 1.1, 1.2, 1.3, 1.4], 0.15, True),
    ([-1.0, 1.0], 1.5, False),
    ([-1.0, -1.1], 0.05, False),
    ([0.0, 0.1, 0.2], 0.2, True),
    ([float("inf"), float("inf")], 0.1, False),
    ([-float("inf"), float("inf")], 1.0, False),
])
def test_has_close_elements(numbers, threshold, expected):
    assert has_close_elements(numbers, threshold) == expected


@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    123,
    [1, "2", 3],
    [[], []],
])
def test_has_close_elements_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        has_close_elements(invalid_input, 1.0)


def test_has_close_elements_invalid_threshold():
    with pytest.raises((TypeError, ValueError)):
        has_close_elements([1.0, 2.0], "invalid")


def test_has_close_elements_negative_threshold():
    result = has_close_elements([1.0, 2.0], -1.0)
    assert result == False


def test_has_close_elements_zero_threshold():
    assert has_close_elements([1.0, 1.0], 0.0) == False
    assert has_close_elements([1.0, 1.1], 0.0) == False