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

def fruit_distribution(s: str, n: int) -> int:
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)

def test_fruit_distribution_normal_cases():
    assert fruit_distribution('5 2 3', 10) == 0
    assert fruit_distribution('1 2', 5) == 2
    assert fruit_distribution('0 0 0', 10) == 10

def test_fruit_distribution_edge_cases():
    assert fruit_distribution('', 5) == 5
    assert fruit_distribution('0', 10) == 10
    assert fruit_distribution('9', 10) == 1

@pytest.mark.parametrize("s,n,expected", [
    ('5 2 3', 10, 0),
    ('1 2', 5, 2),
    ('0 0 0', 10, 10),
    ('', 5, 5),
    ('0', 10, 10),
    ('9', 10, 1)
])
def test_fruit_distribution_parametrized(s, n, expected):
    assert fruit_distribution(s, n) == expected

def test_fruit_distribution_large_numbers():
    assert fruit_distribution('1000 2000', 5000) == 2000

def test_fruit_distribution_mixed_input():
    assert fruit_distribution('5 apple 3 banana', 15) == 7
