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

def test_basic_fruit_distribution():
    assert fruit_distribution("5 2 3", 10) == 0
    assert fruit_distribution("2 3 4", 15) == 6

@pytest.mark.parametrize("s,n,expected", [
    ("1 2 3", 10, 4),
    ("5 5 5", 20, 5),
    ("1", 5, 4),
    ("10 20 30", 100, 40),
    ("0", 5, 5),
    ("1 2 three 4", 10, 3),
    ("", 5, 5),
    ("abc def ghi", 10, 10),
    ("1 a 2 b 3", 10, 4),
    ("0 0 0", 5, 5)
])
def test_fruit_distribution_parametrized(s, n, expected):
    assert fruit_distribution(s, n) == expected

def test_zero_total():
    assert fruit_distribution("0", 0) == 0

def test_large_numbers():
    assert fruit_distribution("1000 2000 3000", 10000) == 4000

def test_whitespace_handling():
    assert fruit_distribution("  1   2   3  ", 10) == 4
    assert fruit_distribution("1 2 3", 10) == 4

def test_negative_result():
    assert fruit_distribution("10 20", 5) == -25

def test_single_space():
    assert fruit_distribution(" ", 5) == 5

def test_special_characters():
    assert fruit_distribution("1 @ 2 # 3 $", 10) == 4

def test_repeated_numbers():
    assert fruit_distribution("1 1 1 1 1", 10) == 5