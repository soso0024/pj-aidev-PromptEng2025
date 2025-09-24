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
    if need <= remaining:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]

def test_eat_sufficient_remaining():
    assert eat(10, 5, 10) == [15, 5]

def test_eat_insufficient_remaining():
    assert eat(10, 15, 10) == [20, 0]

@pytest.mark.parametrize("number,need,remaining,expected", [
    (10, 0, 10, [10, 10]),
    (10, 10, 10, [20, 0]),
    (10, 5, 0, [15, 0]),
    (0, 5, 0, [5, 0]),
    (0, 0, 0, [0, 0])
])
def test_eat_with_various_inputs(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_eat_with_negative_need():
    with pytest.raises(ValueError):
        eat(10, -5, 10)

def test_eat_with_negative_remaining():
    with pytest.raises(ValueError):
        eat(10, 5, -10)