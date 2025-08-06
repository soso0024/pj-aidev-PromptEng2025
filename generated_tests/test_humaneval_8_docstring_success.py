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
    ([1, 2], (3, 2)),
    ([1, 2, 3, 4], (10, 24)),
    ([-1, -2, -3], (-6, -6)),
    ([0], (0, 0)),
    ([0, 1, 2], (3, 0)),
    ([-1, 1], (0, -1)),
    ([100, 200], (300, 20000)),
])
def test_sum_product_valid_inputs(numbers: List[int], expected: Tuple[int, int]):
    assert sum_product(numbers) == expected


def test_sum_product_empty_list():
    assert sum_product([]) == (0, 1)


@pytest.mark.parametrize("invalid_input", [
    None,
    "string",
    [1, "2", 3],
    [[1, 2], [3, 4]],
])
def test_sum_product_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        sum_product(invalid_input)


def test_sum_product_large_numbers():
    assert sum_product([1000, 1000, 1000]) == (3000, 1000000000)


def test_sum_product_single_zero():
    assert sum_product([0]) == (0, 0)


def test_sum_product_multiple_zeros():
    assert sum_product([0, 0, 0]) == (0, 0)


def test_sum_product_mixed_signs():
    assert sum_product([-2, 3, -4]) == (-3, 24)