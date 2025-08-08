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

def test_car_race_collision_zero():
    assert car_race_collision(0) == 0

def test_car_race_collision_one():
    assert car_race_collision(1) == 1

def test_car_race_collision_positive():
    assert car_race_collision(5) == 25

@pytest.mark.parametrize("input_n,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (10, 100)
])
def test_car_race_collision_multiple_cases(input_n, expected):
    assert car_race_collision(input_n) == expected

def test_car_race_collision_large_number():
    assert car_race_collision(1000) == 1000000

@pytest.mark.parametrize("invalid_input", [
    "string",
    None,
    [],
    {}
])
def test_car_race_collision_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        car_race_collision(invalid_input)

def test_car_race_collision_negative():
    result = car_race_collision(-5)
    assert result == 25

def test_car_race_collision_float():
    result = car_race_collision(3.14)
    assert result == pytest.approx(9.8596)