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

def test_fruit_distribution_empty_string():
    assert fruit_distribution('', 10) == 10

def test_fruit_distribution_all_digits():
    assert fruit_distribution('1 2 3', 10) == 4

def test_fruit_distribution_mixed_input():
    assert fruit_distribution('1 apple 2 banana', 10) == 7

def test_fruit_distribution_negative_n():
    assert fruit_distribution('1 2 3', -5) == -8

@pytest.mark.parametrize("s,n,expected", [
    ('', 0, 0),
    ('1 2 3', 10, 4),
    ('1 apple 2 banana', 10, 7),
    ('1 2 3', -5, -8)
])
def test_fruit_distribution_parametrized(s, n, expected):
    assert fruit_distribution(s, n) == expected

def test_fruit_distribution_type_error():
    with pytest.raises(TypeError):
        fruit_distribution(123, 'abc')

def fruit_distribution(s, n):
    if isinstance(s, str):
        lis = list()
        for i in s.split(' '):
            if i.isdigit():
                lis.append(int(i))
        return n - sum(lis)
    else:
        raise TypeError("Input 's' must be a string")