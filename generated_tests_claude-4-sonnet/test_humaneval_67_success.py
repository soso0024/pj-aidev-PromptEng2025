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
    ("5 apples and 6 oranges", 11, 0),
    ("1 apple and 2 oranges", 10, 7),
    ("10 bananas and 20 grapes", 50, 20),
    ("0 fruits", 5, 5),
    ("", 10, 10),
    ("no numbers here", 15, 15),
    ("123 apples", 200, 77),
    ("1 apple 2 oranges 3 bananas", 20, 14),
    ("999 apples and 1 orange", 1000, 0),
    ("50 apples and 50 oranges", 100, 0)
])
def test_fruit_distribution_parametrized(s, n, expected):
    assert fruit_distribution(s, n) == expected

def test_empty_string():
    assert fruit_distribution("", 0) == 0

def test_only_spaces():
    assert fruit_distribution("   ", 5) == 5

def test_single_number():
    assert fruit_distribution("42", 50) == 8

def test_multiple_spaces():
    assert fruit_distribution("5  apples   and    6   oranges", 20) == 9

def test_large_numbers():
    assert fruit_distribution("1000000 apples and 2000000 oranges", 5000000) == 2000000

def test_zero_total():
    assert fruit_distribution("5 apples and 5 oranges", 10) == 0

def test_negative_result():
    assert fruit_distribution("10 apples and 20 oranges", 25) == -5

def test_no_fruits_mentioned():
    assert fruit_distribution("apples and oranges", 100) == 100

def test_mixed_text_and_numbers():
    assert fruit_distribution("I have 5 apples and my friend has 3 oranges", 10) == 2

def test_numbers_at_end():
    assert fruit_distribution("apples 10 oranges 20", 50) == 20

def test_single_digit_numbers():
    assert fruit_distribution("1 apple 2 oranges 3 bananas 4 grapes", 15) == 5

def test_zero_fruits():
    assert fruit_distribution("0 apples and 0 oranges", 10) == 10
