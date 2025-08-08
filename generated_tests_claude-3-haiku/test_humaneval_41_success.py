# Test cases for HumanEval/41
# Generated using Claude API



def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """

    return n**2


# Generated test cases:
import pytest

def test_car_race_collision_positive_integers():
    assert car_race_collision(1) == 1
    assert car_race_collision(5) == 25
    assert car_race_collision(10) == 100

def test_car_race_collision_zero():
    assert car_race_collision(0) == 0

def test_car_race_collision_negative_integers():
    with pytest.raises(ValueError):
        car_race_collision(-1)
        car_race_collision(-5)
        car_race_collision(-10)

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (5, 25),
    (10, 100),
    (0, 0),
    (-1, ValueError),
    (-5, ValueError),
    (-10, ValueError)
])
def test_car_race_collision_parametrized(input, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            car_race_collision(input)
    else:
        assert car_race_collision(input) == expected

def car_race_collision(n: int):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return n**2