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

def test_fruit_distribution_basic():
    assert fruit_distribution("3 apples and 2 oranges", 10) == 5
    assert fruit_distribution("1 apples and 1 oranges", 5) == 3
    assert fruit_distribution("0 apples and 0 oranges", 5) == 5

@pytest.mark.parametrize("s,n,expected", [
    ("5 apples and 2 oranges", 15, 8),
    ("1 apples and 0 oranges", 10, 9),
    ("0 apples and 0 oranges", 5, 5),
    ("10 apples and 0 oranges", 10, 0),
    ("1 apples and 2 oranges", 20, 17),
    ("0 apples and 0 oranges", 5, 5),
    ("0 apples and 0 oranges", 0, 0),
    ("non-numeric 5 apples and 3 oranges", 10, 2),
    ("1 apples and 2 oranges", 20, 17),
    ("   1 apples and   2   oranges   ", 10, 7)
])
def test_fruit_distribution_parametrized(s, n, expected):
    assert fruit_distribution(s, n) == expected

def test_fruit_distribution_large_numbers():
    assert fruit_distribution("100 apples and 200 oranges", 1000) == 700
    assert fruit_distribution("999 apples and 999 oranges", 3000) == 1002

def test_fruit_distribution_special_chars():
    assert fruit_distribution("1 apples and 2 oranges!", 10) == 7
    assert fruit_distribution("$1 apples and 2 oranges", 10) == 8

def test_fruit_distribution_whitespace():
    assert fruit_distribution("   ", 5) == 5
    assert fruit_distribution("\t\n", 5) == 5
    assert fruit_distribution(" 1 apples and 2 oranges ", 10) == 7

@pytest.mark.parametrize("s,n", [
    ("abc", -1),
    ("1 apples and 2 oranges", -5),
    ("-1 apples and 2 oranges", 0),
    ("1.5 apples and 2.7 oranges", 10)
])
def test_fruit_distribution_edge_cases(s, n):
    result = fruit_distribution(s, n)
    assert isinstance(result, int)