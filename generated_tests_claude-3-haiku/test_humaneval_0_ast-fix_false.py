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

def test_has_close_elements_empty_list():
    assert not has_close_elements([], 0.1)

def test_has_close_elements_single_element():
    assert not has_close_elements([1.0], 0.1)

def test_has_close_elements_all_close():
    assert has_close_elements([1.0, 1.01, 1.02], 0.1)

def test_has_close_elements_some_close():
    assert has_close_elements([1.0, 1.01, 2.0], 0.1)

def test_has_close_elements_no_close():
    assert not has_close_elements([1.0, 2.0, 3.0], 0.1)

def test_has_close_elements_threshold_zero():
    assert not has_close_elements([1.0, 1.0, 1.0], 0.0)

def test_has_close_elements_threshold_negative():
    with pytest.raises(ValueError):
        has_close_elements([1.0, 1.0, 1.0], -0.1)

@pytest.mark.parametrize("numbers,threshold,expected", [
    ([1.0, 1.01, 1.02], 0.1, True),
    ([1.0, 1.01, 2.0], 0.1, True),
    ([1.0, 2.0, 3.0], 0.1, False),
    ([], 0.1, False),
    ([1.0], 0.1, False),
    ([1.0, 1.0, 1.0], 0.0, False),
    ([1.0, 1.0, 1.0], -0.1, pytest.raises(ValueError))
])
def test_has_close_elements_parametrized(numbers, threshold, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            has_close_elements(numbers, threshold)
    else:
        assert has_close_elements(numbers, threshold) == expected

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    if threshold < 0:
        raise ValueError("Threshold cannot be negative")

    for i, elem in enumerate(numbers):
        for j, elem2 in enumerate(numbers):
            if i != j:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False