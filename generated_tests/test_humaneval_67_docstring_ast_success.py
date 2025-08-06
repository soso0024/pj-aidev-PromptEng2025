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
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95

@pytest.mark.parametrize("s,n,expected", [
    ("100 apples and 1 oranges", 120, 19),
    ("0 apples and 0 oranges", 5, 5),
    ("1 apples and 1 oranges", 3, 1),
    ("50 apples and 50 oranges", 150, 50),
    ("1 apples and 99 oranges", 200, 100)
])
def test_parametrized_fruit_distribution(s, n, expected):
    assert fruit_distribution(s, n) == expected

@pytest.mark.parametrize("s,n", [
    ("no numbers here", 10),
    ("", 5),
    ("apples and oranges", 3)
])
def test_no_numbers_fruit_distribution(s, n):
    assert fruit_distribution(s, n) == n

def test_large_numbers():
    assert fruit_distribution("1000 apples and 2000 oranges", 5000) == 2000
    assert fruit_distribution("999999 apples and 999999 oranges", 2000000) == 2

def test_zero_total_fruits():
    assert fruit_distribution("0 apples and 0 oranges", 0) == 0

@pytest.mark.parametrize("s,n", [
    ("10 apples and 20 oranges", -1),
    ("5 apples and 3 oranges", 7)
])
def test_invalid_total_fruits(s, n):
    result = fruit_distribution(s, n)
    assert result < 0

def test_whitespace_handling():
    assert fruit_distribution("  5   apples    and   6    oranges  ", 15) == 4
    assert fruit_distribution("1 apples and 2 oranges", 5) == 2

def test_multiple_numbers():
    assert fruit_distribution("1 2 3 apples and 4 5 6 oranges", 21) == 0

def test_special_characters():
    assert fruit_distribution("1 apples and 2 oranges", 5) == 2
    assert fruit_distribution("1 apples and 2 oranges", 5) == 2