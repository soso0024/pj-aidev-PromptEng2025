# Test cases for HumanEval/8
# Generated using Claude API

from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value


# Generated test cases:
import pytest
from typing import List

def sum_product(numbers: List[int]):
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

def test_empty_list():
    result = sum_product([])
    assert result == (0, 1)

def test_single_element():
    result = sum_product([5])
    assert result == (5, 5)

def test_single_zero():
    result = sum_product([0])
    assert result == (0, 0)

def test_multiple_positive_numbers():
    result = sum_product([1, 2, 3, 4])
    assert result == (10, 24)

def test_multiple_negative_numbers():
    result = sum_product([-1, -2, -3])
    assert result == (-6, -6)

def test_mixed_positive_negative():
    result = sum_product([1, -2, 3, -4])
    assert result == (-2, 24)

def test_with_zero_in_middle():
    result = sum_product([1, 2, 0, 3, 4])
    assert result == (10, 0)

def test_all_zeros():
    result = sum_product([0, 0, 0])
    assert result == (0, 0)

def test_large_numbers():
    result = sum_product([100, 200, 300])
    assert result == (600, 6000000)

def test_negative_and_zero():
    result = sum_product([-5, 0, 10])
    assert result == (5, 0)

@pytest.mark.parametrize("numbers,expected", [
    ([1], (1, 1)),
    ([2, 3], (5, 6)),
    ([-1, 1], (0, -1)),
    ([10, -10], (0, -100)),
    ([1, 1, 1, 1], (4, 1))
])
def test_parametrized_cases(numbers, expected):
    assert sum_product(numbers) == expected

def test_very_large_list():
    numbers = [1] * 1000
    result = sum_product(numbers)
    assert result == (1000, 1)

def test_alternating_ones_and_negative_ones():
    result = sum_product([1, -1, 1, -1])
    assert result == (0, 1)
