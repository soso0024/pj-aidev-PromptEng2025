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

def test_sum_product_empty_list():
    from typing import List
    def sum_product(numbers: List[int]):
        sum_value = 0
        prod_value = 1

        for n in numbers:
            sum_value += n
            prod_value *= n
        return sum_value, prod_value

    assert sum_product([]) == (0, 1)

def test_sum_product_single_element():
    def sum_product(numbers: List[int]):
        sum_value = 0
        prod_value = 1

        for n in numbers:
            sum_value += n
            prod_value *= n
        return sum_value, prod_value

    assert sum_product([5]) == (5, 5)

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3], (6, 6)),
    ([0, 0, 0], (0, 0)),
    ([-1, 2, -3], (-2, 6)),
    ([10, 20, 30], (60, 6000))
])
def test_sum_product_various_inputs(input, expected):
    def sum_product(numbers: List[int]):
        sum_value = 0
        prod_value = 1

        for n in numbers:
            sum_value += n
            prod_value *= n
        return sum_value, prod_value

    assert sum_product(input) == expected

def test_sum_product_non_integer_input():
    def sum_product(numbers: List[int]):
        sum_value = 0
        prod_value = 1

        for n in numbers:
            sum_value += n
            prod_value *= n
        return sum_value, prod_value

    with pytest.raises(TypeError):
        sum_product([1, 2, 'a'])
