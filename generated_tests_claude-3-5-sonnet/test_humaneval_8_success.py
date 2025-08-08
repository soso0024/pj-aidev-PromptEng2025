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
    ([1, 2, 3], (6, 6)),
    ([0, 1, 2], (3, 0)),
    ([1, 1, 1], (3, 1)),
    ([-1, 2, -3], (-2, 6)),
    ([], (0, 1)),
    ([5], (5, 5)),
    ([-2, -2], (-4, 4)),
    ([0, 0, 0], (0, 0)),
    ([10, -10], (0, -100)),
    ([1, 2, 3, 4, 5], (15, 120))
])
def test_sum_product_valid_inputs(numbers: List[int], expected: Tuple[int, int]):
    assert sum_product(numbers) == expected

def test_sum_product_none_input():
    with pytest.raises(TypeError):
        sum_product(None)

def test_sum_product_invalid_type():
    with pytest.raises(TypeError):
        sum_product("not a list")

def test_sum_product_invalid_elements():
    with pytest.raises(TypeError):
        sum_product([1, "2", 3])

def test_sum_product_nested_list():
    with pytest.raises(TypeError):
        sum_product([1, [2, 3], 4])

def test_sum_product_float_elements():
    with pytest.raises(TypeError):
        sum_product([1.5, 2, 3])

def test_sum_product_large_numbers():
    result = sum_product([1000000, 1000000])
    assert result == (2000000, 1000000000000)

def test_sum_product_single_zero():
    assert sum_product([0]) == (0, 0)

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if numbers is None:
        raise TypeError("Input cannot be None")
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements must be integers")
    
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value