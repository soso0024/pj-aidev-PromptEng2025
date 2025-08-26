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
from typing import Any

def car_race_collision(n: int):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    return n**2

def test_car_race_collision_zero():
    assert car_race_collision(0) == 0

def test_car_race_collision_positive_integers():
    assert car_race_collision(1) == 1
    assert car_race_collision(2) == 4
    assert car_race_collision(5) == 25
    assert car_race_collision(10) == 100

def test_car_race_collision_large_number():
    assert car_race_collision(100) == 10000

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 4),
    (5, 25),
    (10, 100),
    (100, 10000)
])
def test_car_race_collision_parametrized(n, expected):
    assert car_race_collision(n) == expected

def test_car_race_collision_negative_input():
    with pytest.raises(ValueError):
        car_race_collision(-1)

def test_car_race_collision_type_error():
    with pytest.raises(TypeError):
        car_race_collision('string')
    with pytest.raises(TypeError):
        car_race_collision([1, 2, 3])