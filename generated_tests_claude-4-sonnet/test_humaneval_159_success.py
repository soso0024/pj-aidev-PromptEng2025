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

def eat(number, need, remaining):
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]

def test_eat_enough_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_exact_remaining():
    assert eat(5, 6, 6) == [11, 0]

def test_eat_not_enough_remaining():
    assert eat(5, 6, 4) == [9, 0]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_zero_number():
    assert eat(0, 6, 10) == [6, 4]

def test_eat_all_zeros():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_large_numbers():
    assert eat(1000, 500, 2000) == [1500, 1500]

def test_eat_large_need_small_remaining():
    assert eat(100, 1000, 50) == [150, 0]

@pytest.mark.parametrize("number,need,remaining,expected", [
    (10, 5, 20, [15, 15]),
    (0, 10, 5, [5, 0]),
    (100, 0, 50, [100, 50]),
    (1, 1, 1, [2, 0]),
    (50, 25, 25, [75, 0]),
    (7, 3, 10, [10, 7])
])
def test_eat_parametrized(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_eat_negative_numbers():
    assert eat(-5, 10, 15) == [5, 5]

def test_eat_negative_need():
    assert eat(10, -5, 20) == [5, 25]

def test_eat_negative_remaining():
    assert eat(10, 5, -3) == [7, 0]

def test_eat_float_inputs():
    assert eat(5.5, 2.5, 10.0) == [8.0, 7.5]

def test_eat_float_not_enough():
    assert eat(5.5, 10.5, 3.2) == [8.7, 0]
