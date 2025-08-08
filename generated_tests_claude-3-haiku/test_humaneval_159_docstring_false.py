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

@pytest.mark.parametrize("number, need, remaining, expected", [
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    (0, 10, 10, [10, 0]),
    (1000, 1000, 1000, [2000, 0]),
    (0, 0, 0, [0, 0]),
    (0, 10, 10, pytest.raises(ValueError)),
    (10, 0, 10, pytest.raises(ValueError)),
    (10, 10, 0, pytest.raises(ValueError))
])
def test_eat(number, need, remaining, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            assert eat(number, need, remaining) == expected
    else:
        assert eat(number, need, remaining) == expected

def eat(number, need, remaining):
    if number < 0 or need < 0 or remaining < 0:
        raise ValueError("Input values must be non-negative integers")
    if need <= remaining:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]