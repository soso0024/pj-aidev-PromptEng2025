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
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

def test_empty_list():
    assert sum_product([]) == (0, 1)

def test_single_element_list():
    assert sum_product([5]) == (5, 5)

def test_multiple_elements_list():
    assert sum_product([1, 2, 3, 4]) == (10, 24)

def test_list_with_zero():
    assert sum_product([0, 1, 2, 3]) == (6, 0)

def test_list_with_negative_numbers():
    assert sum_product([-1, -2, -3]) == (-6, -6)

def test_list_with_mixed_numbers():
    assert sum_product([-1, 0, 1, 2]) == (2, 0)

@pytest.mark.parametrize("input_list,expected", [
    ([], (0, 1)),
    ([5], (5, 5)),
    ([1, 2, 3, 4], (10, 24)),
    ([0, 1, 2, 3], (6, 0)),
    ([-1, -2, -3], (-6, -6)),
    ([-1, 0, 1, 2], (2, 0))
])
def test_sum_product_parametrized(input_list, expected):
    assert sum_product(input_list) == expected
