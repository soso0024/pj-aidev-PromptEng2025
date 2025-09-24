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
    assert has_close_elements([], 0.1) == False

def test_single_element():
    assert has_close_elements([1.0], 0.1) == False

def test_two_elements_close():
    assert has_close_elements([1.0, 1.05], 0.1) == True

def test_two_elements_not_close():
    assert has_close_elements([1.0, 2.0], 0.5) == False

def test_two_elements_exactly_threshold():
    assert has_close_elements([1.0, 1.5], 0.5) == False

def test_two_elements_just_under_threshold():
    assert has_close_elements([1.0, 1.49], 0.5) == True

def test_multiple_elements_with_close_pair():
    assert has_close_elements([1.0, 5.0, 3.0, 3.1], 0.2) == True

def test_multiple_elements_no_close_pairs():
    assert has_close_elements([1.0, 3.0, 5.0, 7.0], 1.5) == False

def test_negative_numbers():
    assert has_close_elements([-1.0, -1.1], 0.2) == True

def test_mixed_positive_negative():
    assert has_close_elements([-1.0, 1.0], 1.5) == False

def test_zero_threshold():
    assert has_close_elements([1.0, 1.0], 0.0) == False

def test_identical_elements_positive_threshold():
    assert has_close_elements([1.0, 1.0], 0.1) == True

def test_very_small_threshold():
    assert has_close_elements([1.0, 1.000001], 0.000001) == True

def test_very_large_numbers():
    assert has_close_elements([1000000.0, 1000000.1], 0.2) == True

def test_zero_values():
    assert has_close_elements([0.0, 0.0], 0.1) == True

def test_zero_and_small_positive():
    assert has_close_elements([0.0, 0.05], 0.1) == True

def test_many_identical_elements():
    assert has_close_elements([2.0, 2.0, 2.0, 2.0], 0.1) == True

def test_large_list_no_close_elements():
    numbers = [i * 2.0 for i in range(10)]
    assert has_close_elements(numbers, 1.0) == False

def test_large_list_with_close_elements():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 5.1]
    assert has_close_elements(numbers, 0.2) == True

@pytest.mark.parametrize("numbers,threshold,expected", [
    ([1.0, 2.0], 0.5, False),
    ([1.0, 1.4], 0.5, True),
    ([1.0, 1.5], 0.5, False),
    ([0.0, 0.1], 0.2, True),
    ([-1.0, -0.9], 0.2, True),
    ([10.0, 20.0, 30.0], 5.0, False),
    ([1.1, 1.2, 1.3], 0.15, True)
])
def test_parametrized_cases(numbers, threshold, expected):
    assert has_close_elements(numbers, threshold) == expected

def test_floating_point_precision():
    assert has_close_elements([0.1 + 0.2, 0.3], 0.0000001) == True

def test_negative_threshold():
    assert has_close_elements([1.0, 2.0], -0.5) == False

def test_very_close_different_numbers():
    assert has_close_elements([1.0000001, 1.0000002], 0.000001) == True