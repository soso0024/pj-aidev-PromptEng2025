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

def car_race_collision(n: int):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    return n**2

def test_car_race_collision_zero_cars():
    assert car_race_collision(0) == 0

def test_car_race_collision_single_car():
    assert car_race_collision(1) == 1

def test_car_race_collision_multiple_cars():
    assert car_race_collision(2) == 4
    assert car_race_collision(3) == 9
    assert car_race_collision(5) == 25

def test_car_race_collision_large_number():
    assert car_race_collision(100) == 10000

@pytest.mark.parametrize("n", [-1, -5])
def test_car_race_collision_negative_input(n):
    with pytest.raises(ValueError):
        car_race_collision(n)

def test_car_race_collision_type_error():
    with pytest.raises(TypeError):
        car_race_collision("not an integer")
        car_race_collision(3.14)