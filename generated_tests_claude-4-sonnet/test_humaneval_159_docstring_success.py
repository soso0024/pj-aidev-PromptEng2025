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

@pytest.mark.parametrize("number,need,remaining,expected", [
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    (0, 0, 0, [0, 0]),
    (0, 5, 10, [5, 5]),
    (10, 0, 5, [10, 5]),
    (5, 10, 0, [5, 0]),
    (1000, 1000, 1000, [2000, 0]),
    (0, 1000, 1000, [1000, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (1000, 1000, 0, [1000, 0]),
    (500, 300, 400, [800, 100]),
    (100, 200, 150, [250, 0]),
    (1, 1, 1, [2, 0]),
    (999, 1, 1000, [1000, 999]),
    (1, 999, 1000, [1000, 1]),
    (0, 1, 0, [0, 0]),
    (1, 0, 0, [1, 0]),
    (50, 25, 100, [75, 75])
])
def test_eat_parametrized(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_eat_enough_carrots():
    result = eat(5, 6, 10)
    assert result == [11, 4]
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)

def test_eat_not_enough_carrots():
    result = eat(2, 11, 5)
    assert result == [7, 0]
    assert len(result) == 2

def test_eat_exact_amount():
    result = eat(1, 10, 10)
    assert result == [11, 0]

def test_eat_zero_values():
    assert eat(0, 0, 0) == [0, 0]
    assert eat(0, 0, 10) == [0, 10]
    assert eat(5, 0, 0) == [5, 0]
    assert eat(0, 5, 0) == [0, 0]

def test_eat_boundary_values():
    assert eat(1000, 1000, 1000) == [2000, 0]
    assert eat(0, 1000, 1000) == [1000, 0]
    assert eat(1000, 0, 1000) == [1000, 1000]

def test_eat_return_type():
    result = eat(1, 1, 1)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
