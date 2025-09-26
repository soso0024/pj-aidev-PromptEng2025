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
                if distance < threshold:
                    return True
    return False

def test_empty_list():
    assert has_close_elements([], 0.5) == False

def test_single_element():
    assert has_close_elements([1.0], 0.5) == False

def test_two_elements_close():
    assert has_close_elements([1.0, 1.2], 0.5) == True

def test_two_elements_not_close():
    assert has_close_elements([1.0, 2.0], 0.5) == False

def test_two_elements_exactly_threshold():
    assert has_close_elements([1.0, 1.5], 0.5) == False

def test_multiple_elements_no_close_pairs():
    assert has_close_elements([1.0, 2.0, 3.0, 4.0], 0.5) == False

def test_multiple_elements_with_close_pairs():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True

def test_identical_elements():
    assert has_close_elements([1.0, 1.0], 0.1) == True

def test_negative_numbers():
    assert has_close_elements([-1.0, -1.2, -3.0], 0.3) == True

def test_mixed_positive_negative():
    assert has_close_elements([-1.0, 1.0, 2.0], 0.5) == False

def test_zero_threshold():
    assert has_close_elements([1.0, 2.0], 0.0) == False

def test_zero_threshold_identical():
    assert has_close_elements([1.0, 1.0], 0.0) == False

def test_very_small_threshold():
    assert has_close_elements([1.0, 1.00001], 0.00001) == False

def test_very_large_threshold():
    assert has_close_elements([1.0, 100.0], 200.0) == True

def test_floating_point_precision():
    assert has_close_elements([0.1, 0.2, 0.3], 0.05) == False

@pytest.mark.parametrize("numbers,threshold,expected", [
    ([1.0, 2.0, 3.0], 0.5, False),
    ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
    ([1.0, 1.1], 0.2, True),
    ([1.0, 1.1], 0.05, False),
    ([0.0, 0.0], 1.0, True),
    ([-5.0, -4.9], 0.2, True),
    ([10.0, 20.0, 30.0], 5.0, False)
])
def test_parametrized_cases(numbers, threshold, expected):
    assert has_close_elements(numbers, threshold) == expected

def test_large_list():
    numbers = [i * 2.0 for i in range(100)]
    assert has_close_elements(numbers, 1.0) == False

def test_large_list_with_close_elements():
    numbers = [i * 2.0 for i in range(100)]
    numbers.append(1.5)
    assert has_close_elements(numbers, 1.0) == True