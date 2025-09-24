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

def test_single_element():
    assert sum_product([5]) == (5, 5)
    assert sum_product([0]) == (0, 0)
    assert sum_product([-3]) == (-3, -3)

def test_multiple_positive_numbers():
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([2, 4, 6]) == (12, 48)

def test_multiple_negative_numbers():
    assert sum_product([-1, -2, -3]) == (-6, -6)
    assert sum_product([-2, -4]) == (-6, 8)

def test_mixed_positive_negative():
    assert sum_product([1, -2, 3]) == (2, -6)
    assert sum_product([-1, 2, -3, 4]) == (2, 24)

def test_with_zero():
    assert sum_product([1, 0, 3]) == (4, 0)
    assert sum_product([0, 0, 0]) == (0, 0)
    assert sum_product([5, 0, -2]) == (3, 0)

def test_large_numbers():
    assert sum_product([100, 200, 300]) == (600, 6000000)
    assert sum_product([1000, -500]) == (500, -500000)

@pytest.mark.parametrize("numbers,expected", [
    ([1], (1, 1)),
    ([2, 3], (5, 6)),
    ([1, 1, 1], (3, 1)),
    ([-1, -1], (-2, 1)),
    ([10, -10], (0, -100))
])
def test_parametrized_cases(numbers, expected):
    assert sum_product(numbers) == expected
