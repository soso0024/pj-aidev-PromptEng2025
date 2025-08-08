# Test cases for HumanEval/159
# Generated using Claude API


def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """

    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]


# Generated test cases:
import pytest

def test_eat_basic():
    assert eat(5, 3, 10) == [8, 7]
    assert eat(10, 5, 20) == [15, 15]

def test_eat_exact_remaining():
    assert eat(0, 10, 10) == [10, 0]
    assert eat(5, 5, 5) == [10, 0]

def test_eat_not_enough_remaining():
    assert eat(10, 20, 5) == [15, 0]
    assert eat(0, 100, 50) == [50, 0]

def test_eat_zero_need():
    assert eat(10, 0, 5) == [10, 5]
    assert eat(0, 0, 10) == [0, 10]

def test_eat_zero_remaining():
    assert eat(5, 10, 0) == [5, 0]
    assert eat(0, 20, 0) == [0, 0]

@pytest.mark.parametrize("number, need, remaining, expected", [
    (0, 5, 10, [5, 5]),
    (10, 5, 3, [13, 0]),
    (100, 50, 25, [125, 0]),
    (0, 0, 0, [0, 0]),
    (1000, 2000, 1500, [2500, 0]),
    (50, 25, 25, [75, 0]),
    (10, 10, 20, [20, 10])
])
def test_eat_parametrized(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_eat_large_numbers():
    assert eat(1000000, 500000, 1000000) == [1500000, 500000]
    assert eat(999999, 1000000, 500000) == [1499999, 0]

def test_eat_small_numbers():
    assert eat(1, 1, 1) == [2, 0]
    assert eat(1, 2, 1) == [2, 0]
