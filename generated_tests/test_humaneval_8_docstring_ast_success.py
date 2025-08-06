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


@pytest.mark.parametrize("numbers,expected", [
    ([], (0, 1)),
    ([1], (1, 1)),
    ([1, 2, 3, 4], (10, 24)),
    ([-1, -2, -3], (-6, -6)),
    ([0], (0, 0)),
    ([1, 0, 2], (3, 0)),
    ([-1, 1], (0, -1)),
    ([100, 200], (300, 20000)),
])
def test_sum_product_valid_inputs(numbers: List[int], expected: Tuple[int, int], sum_product):
    assert sum_product(numbers) == expected


def test_sum_product_empty_list(sum_product):
    assert sum_product([]) == (0, 1)


@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    [1, "2", 3],
    {"a": 1, "b": 2},
])
def test_sum_product_invalid_inputs(invalid_input, sum_product):
    with pytest.raises((TypeError, AttributeError)):
        sum_product(invalid_input)


def test_sum_product_large_numbers(sum_product):
    numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
    assert sum_product(numbers) == (15, 120)


def test_sum_product_all_zeros(sum_product):
    assert sum_product([0, 0, 0]) == (0, 0)


def test_sum_product_single_negative(sum_product):
    assert sum_product([-5]) == (-5, -5)


def test_sum_product_alternating_signs(sum_product):
    assert sum_product([1, -1, 1, -1]) == (0, 1)


@pytest.fixture
def sum_product():
    def _sum_product(numbers: List[int]) -> Tuple[int, int]:
        sum_value = 0
        prod_value = 1
        for n in numbers:
            sum_value += n
            prod_value *= n
        return sum_value, prod_value
    return _sum_product