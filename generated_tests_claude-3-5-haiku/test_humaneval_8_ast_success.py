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

def test_sum_product_normal_case():
    result = sum_product([1, 2, 3, 4])
    assert result == (10, 24)

def test_sum_product_single_element():
    result = sum_product([5])
    assert result == (5, 5)

def test_sum_product_empty_list():
    result = sum_product([])
    assert result == (0, 1)

def test_sum_product_negative_numbers():
    result = sum_product([-1, -2, -3])
    assert result == (-6, -6)

def test_sum_product_mixed_numbers():
    result = sum_product([-1, 2, 3, -4])
    assert result == (0, 24)

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], (6, 6)),
    ([0, 1, 2], (3, 0)),
    ([-5, 5], (0, -25))
])
def test_sum_product_parametrized(input_list, expected):
    assert sum_product(input_list) == expected

def test_sum_product_large_numbers():
    result = sum_product([1000, 2000, 3000])
    assert result == (6000, 6000000000)
