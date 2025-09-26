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

@pytest.mark.parametrize("numbers,expected", [
    ([1, 2, 3], (6, 6)),
    ([0, 1, 2], (3, 0)),
    ([-1, -2, -3], (-6, -6)),
    ([5], (5, 5)),
    ([], (0, 1)),
    ([10, -5, 2], (7, -100)),
    ([1000000, 2000000], (3000000, 2000000000000)),
])
def test_sum_product_normal(numbers, expected):
    assert sum_product(numbers) == expected

def test_sum_product_tuple():
    assert sum_product((4, 5, 6)) == (15, 120)

def test_sum_product_generator():
    gen = (i for i in range(1, 5))
    assert sum_product(gen) == (10, 24)

def test_sum_product_no_side_effect():
    lst = [1, 2, 3]
    lst_copy = lst.copy()
    sum_product(lst)
    assert lst == lst_copy

def test_sum_product_none():
    with pytest.raises(TypeError):
        sum_product(None)

def test_sum_product_non_iterable():
    with pytest.raises(TypeError):
        sum_product(123)

def test_sum_product_non_numeric():
    with pytest.raises(TypeError):
        sum_product([1, "a", 3])

def test_sum_product_return_types():
    result = sum_product([1, 2, 3])
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)

def test_sum_product_large_ints():
    large = 10**100
    result = sum_product([large, large])
    assert result == (2*large, large*large)