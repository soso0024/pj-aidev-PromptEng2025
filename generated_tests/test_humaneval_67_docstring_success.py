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

@pytest.mark.parametrize("s,n,expected", [
    ("5 apples and 6 oranges", 19, 8),
    ("0 apples and 1 oranges", 3, 2),
    ("2 apples and 3 oranges", 100, 95),
    ("100 apples and 1 oranges", 120, 19),
    ("0 apples and 0 oranges", 0, 0),
    ("1 apples and 1 oranges", 5, 3),
    ("10 apples and 10 oranges", 25, 5),
    ("999 apples and 1 oranges", 1500, 500),
])
def test_fruit_distribution_normal_cases(s, n, expected):
    assert fruit_distribution(s, n) == expected

@pytest.mark.parametrize("s,n,expected", [
    ("no apples and no oranges", 5, 5),
    ("apples and oranges", 10, 10),
    ("0 apples and oranges", 3, 3),
    ("apples and 0 oranges", 4, 4),
])
def test_fruit_distribution_no_numbers(s, n, expected):
    assert fruit_distribution(s, n) == expected

@pytest.mark.parametrize("s,n", [
    ("", 5),
    (" ", 3),
    ("apples oranges", 0),
])
def test_fruit_distribution_empty_strings(s, n):
    assert isinstance(fruit_distribution(s, n), int)

def test_fruit_distribution_large_numbers():
    assert fruit_distribution("1000000 apples and 1000000 oranges", 3000000) == 1000000

def test_fruit_distribution_zero_total():
    assert fruit_distribution("0 apples and 0 oranges", 0) == 0

@pytest.mark.parametrize("s,n", [
    ("abc apples and xyz oranges", 10),
    ("!@# apples and $$$ oranges", 5),
])
def test_fruit_distribution_invalid_numbers(s, n):
    assert fruit_distribution(s, n) == n
