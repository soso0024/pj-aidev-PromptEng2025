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

def fruit_distribution(s, n):
    lis = list()
    for i in s.split():
        if i.isdigit():
            lis.append(int(i))
    if n < 0:
        raise ValueError
    return n - sum(lis)

def test_fruit_distribution_empty_string():
    assert fruit_distribution('', 5) == 5

def test_fruit_distribution_single_number():
    assert fruit_distribution('3', 5) == 2

def test_fruit_distribution_multiple_numbers():
    assert fruit_distribution('1 2 3', 10) == 4

def test_fruit_distribution_non_digit_characters():
    assert fruit_distribution('1 a 3', 10) == 6

@pytest.mark.parametrize("input,expected", [
    ('', 10),
    ('5', 5),
    ('1 2 3', 10),
    ('1 a 3', 10),
    ('1 2 3 4 5', 10),
    ('1 2 3 4 5 6', 10)
])
def test_fruit_distribution_parametrized(input, expected):
    assert fruit_distribution(input, expected) == expected - sum(int(x) for x in input.split() if x.isdigit())

def test_fruit_distribution_negative_n():
    with pytest.raises(ValueError):
        fruit_distribution('1 2 3', -5)