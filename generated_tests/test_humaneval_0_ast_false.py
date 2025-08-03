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
    ([1.0, 2.0, 2.1, 4.0], 0.5, True),
    ([1.0, 2.0, 3.0, 4.0], 1.0, False),
    ([], 1.0, False),
    ([1.0], 1.0, False),
    ([1.0, 1.0], 0.5, True),
    ([1.0, 2.0, 2.0, 3.0], 0.1, True),
    ([1.0, 10.0, 100.0, 1000.0], 1.0, False),
    ([0.1, 0.2, 0.3, 0.4], 0.05, False),
    ([0.1, 0.1000001], 0.0001, True),
    ([-1.0, 1.0], 2.1, True),
    ([-10.0, -9.8], 0.3, True),
    ([float("inf"), float("inf")], 1.0, False),
    ([float("-inf"), float("-inf")], 1.0, False),
    ([0.0, -0.0], 0.1, True),
])
def test_has_close_elements_parametrized(numbers: List[float], threshold: float, expected: bool):
    result = has_close_elements(numbers, threshold)
    assert result == expected

def test_has_close_elements_large_list():
    large_list = [float(i) for i in range(1000)]
    assert has_close_elements(large_list, 1.5) == True

@pytest.mark.parametrize("numbers,threshold", [
    (["not_a_float"], 1.0),
    ([None], 1.0),
    ([1.0], "not_a_float"),
    ([1.0], None),
])
def test_has_close_elements_invalid_inputs(numbers, threshold):
    with pytest.raises(TypeError):
        has_close_elements(numbers, threshold)

def test_has_close_elements_negative_threshold():
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0], -1.0)

def test_has_close_elements_zero_threshold():
    assert has_close_elements([1.0, 1.0], 0.0) == False

def test_has_close_elements_nan():
    assert has_close_elements([float('nan'), float('nan')], 1.0) == False

def test_has_close_elements_validation():
    with pytest.raises(TypeError):
        has_close_elements(None, 1.0)
    with pytest.raises(TypeError):
        has_close_elements([1.0], None)
    with pytest.raises(ValueError):
        has_close_elements([1.0], -0.1)