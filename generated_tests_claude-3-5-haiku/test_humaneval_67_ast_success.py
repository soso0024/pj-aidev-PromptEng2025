# Test cases for HumanEval/67
# Generated using Claude API


def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """

    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)


# Generated test cases:
import pytest
from typing import List

def test_fruit_distribution_normal_cases():
    assert fruit_distribution("5 2 3", 10) == 0
    assert fruit_distribution("1 2", 8) == 5
    assert fruit_distribution("0 3", 5) == 2

def test_fruit_distribution_zero_cases():
    assert fruit_distribution("0 0", 10) == 10
    assert fruit_distribution("0", 5) == 5

def test_fruit_distribution_single_number():
    assert fruit_distribution("3", 7) == 4
    assert fruit_distribution("0", 10) == 10

@pytest.mark.parametrize("s,n,expected", [
    ("5 2 3", 10, 0),
    ("1 2", 8, 5),
    ("0 3", 5, 2),
    ("0 0", 10, 10),
    ("0", 5, 5),
    ("3", 7, 4)
])
def test_fruit_distribution_parametrized(s, n, expected):
    assert fruit_distribution(s, n) == expected

def test_fruit_distribution_large_numbers():
    assert fruit_distribution("100 200", 500) == 200
    assert fruit_distribution("1000 2000", 5000) == 2000

def test_fruit_distribution_mixed_whitespace():
    assert fruit_distribution("5  2   3", 10) == 0
    assert fruit_distribution(" 1 2 ", 8) == 5
