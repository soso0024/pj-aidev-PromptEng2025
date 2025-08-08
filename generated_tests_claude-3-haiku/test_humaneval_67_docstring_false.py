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
from solution import fruit_distribution
import pytest

@pytest.mark.parametrize("s,n,expected", [
    ("5 apples and 6 oranges", 19, 8),
    ("0 apples and 1 oranges", 3, 2),
    ("2 apples and 3 oranges", 100, 95),
    ("100 apples and 1 oranges", 120, 19),
    ("", 10, 10),
    ("1 apples and 2 oranges", 3, 0),
    ("10 apples and 20 oranges", 50, 20),
    ("0 apples and 0 oranges", 0, 0),
    ("100 apples and 100 oranges", 200, 0),
    ("abc apples and def oranges", 10, 10),
])
def test_fruit_distribution(s, n, expected):
    assert fruit_distribution(s, n) == expected

def test_fruit_distribution_empty_string():
    with pytest.raises(ValueError):
        fruit_distribution("", 0)

def test_fruit_distribution_negative_n():
    with pytest.raises(ValueError):
        fruit_distribution("1 apples and 2 oranges", -1)