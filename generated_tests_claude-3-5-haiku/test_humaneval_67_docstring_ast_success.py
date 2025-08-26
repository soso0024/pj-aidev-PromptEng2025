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

def test_fruit_distribution_normal_cases():
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19

@pytest.mark.parametrize("s,n,expected", [
    ("5 apples and 6 oranges", 19, 8),
    ("0 apples and 1 oranges", 3, 2),
    ("2 apples and 3 oranges", 100, 95),
    ("100 apples and 1 oranges", 120, 19),
    ("10 apples and 20 oranges", 50, 20),
    ("0 apples and 0 oranges", 100, 100)
])
def test_fruit_distribution_parametrized(s, n, expected):
    assert fruit_distribution(s, n) == expected

def test_fruit_distribution_large_numbers():
    assert fruit_distribution("1000 apples and 2000 oranges", 5000) == 2000

def test_fruit_distribution_single_fruit():
    assert fruit_distribution("1 apples and 0 oranges", 10) == 9

def test_fruit_distribution_no_fruits():
    assert fruit_distribution("0 apples and 0 oranges", 0) == 0
