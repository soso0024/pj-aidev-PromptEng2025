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
    ([1.0, 2.0, 3.0, 4.0], 0.5, False),
    ([1.0, 2.0, 3.0, 4.0], 1.5, True),
    ([1.0, 2.0, 3.0, 4.0], 1.0, True),
    ([], 1.0, False),
    ([1.0], 1.0, False),
    ([1.0, 1.0], 0.5, True),
    ([1.0, 2.0, 2.1], 0.2, True),
    ([1.0, 2.0, 3.0], 0.1, False),
    ([-1.0, 1.0], 2.5, True),
    ([-1.0, -2.0, -3.0], 0.5, False),
    ([0.1, 0.2, 0.3, 0.4], 0.05, False),
    ([1.0, 1.000001], 0.0001, False),
    ([1.0, 1.000001], 0.001, True),
    ([float("inf"), float("inf")], 1.0, True),
    ([-float("inf"), float("inf")], 1.0, False),
])
def test_has_close_elements(numbers, threshold, expected):
    assert has_close_elements(numbers, threshold) == expected

@pytest.mark.parametrize("invalid_input", [
    ("not_a_list", 1.0),
    ([1, "2", 3], 1.0),
    ([1.0, 2.0], "not_a_float"),
    (None, 1.0),
    ([1.0, 2.0], None),
])
def test_has_close_elements_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        has_close_elements(*invalid_input)

def test_has_close_elements_float_precision():
    numbers = [1.0, 1.0 + 1e-10]
    assert has_close_elements(numbers, 1e-9) == True
    assert has_close_elements(numbers, 1e-11) == False

def test_has_close_elements_large_numbers():
    numbers = [1e15, 1e15 + 1]
    assert has_close_elements(numbers, 2.0) == True
    assert has_close_elements(numbers, 0.5) == False
