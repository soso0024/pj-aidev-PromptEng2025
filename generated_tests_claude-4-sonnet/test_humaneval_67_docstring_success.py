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

def fruit_distribution(s,n):
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)

@pytest.mark.parametrize("s,n,expected", [
    ("5 apples and 6 oranges", 19, 8),
    ("0 apples and 1 oranges", 3, 2),
    ("2 apples and 3 oranges", 100, 95),
    ("100 apples and 1 oranges", 120, 19),
    ("10 apples and 20 oranges", 50, 20),
    ("0 apples and 0 oranges", 10, 10),
    ("15 apples and 25 oranges", 40, 0),
    ("1 apples and 1 oranges", 2, 0),
    ("99 apples and 1 oranges", 200, 100),
    ("50 apples and 50 oranges", 150, 50)
])
def test_fruit_distribution_normal_cases(s, n, expected):
    assert fruit_distribution(s, n) == expected

@pytest.mark.parametrize("s,n,expected", [
    ("123 apples and 456 oranges", 1000, 421),
    ("999 apples and 1 oranges", 1500, 500),
    ("1 apples and 999 oranges", 2000, 1000)
])
def test_fruit_distribution_large_numbers(s, n, expected):
    assert fruit_distribution(s, n) == expected

@pytest.mark.parametrize("s,n,expected", [
    ("apples and oranges", 10, 10),
    ("no numbers here", 5, 5),
    ("just words", 20, 20)
])
def test_fruit_distribution_no_numbers(s, n, expected):
    assert fruit_distribution(s, n) == expected

@pytest.mark.parametrize("s,n,expected", [
    ("5 apples", 10, 5),
    ("7 oranges", 15, 8),
    ("3", 8, 5)
])
def test_fruit_distribution_single_number(s, n, expected):
    assert fruit_distribution(s, n) == expected

@pytest.mark.parametrize("s,n,expected", [
    ("1 apples and 2 oranges and 3 bananas", 20, 14),
    ("10 apples and 5 oranges and 2 pears and 1 grape", 50, 32),
    ("0 apples and 0 oranges and 0 bananas", 15, 15)
])
def test_fruit_distribution_multiple_numbers(s, n, expected):
    assert fruit_distribution(s, n) == expected

def test_fruit_distribution_empty_string():
    assert fruit_distribution("", 10) == 10

def test_fruit_distribution_zero_total():
    assert fruit_distribution("0 apples and 0 oranges", 0) == 0

def test_fruit_distribution_negative_result():
    assert fruit_distribution("10 apples and 20 oranges", 25) == -5

def test_fruit_distribution_exact_match():
    assert fruit_distribution("5 apples and 5 oranges", 10) == 0
