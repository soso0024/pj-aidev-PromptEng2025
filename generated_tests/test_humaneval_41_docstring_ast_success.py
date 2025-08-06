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

def test_zero_cars():
    assert car_race_collision(0) == 0

def test_single_car():
    assert car_race_collision(1) == 1

def test_two_cars():
    assert car_race_collision(2) == 4

def test_large_number():
    assert car_race_collision(100) == 10000

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25),
    (10, 100)
])
def test_multiple_cases(n, expected):
    assert car_race_collision(n) == expected

def test_negative_input():
    result = car_race_collision(-1)
    assert result == 1  # -1 squared is 1

def test_type_error():
    with pytest.raises(TypeError):
        car_race_collision("not an integer")

def test_float_input():
    result = car_race_collision(1.5)
    assert result == 2.25  # 1.5 squared is 2.25

def test_none_input():
    with pytest.raises(TypeError):
        car_race_collision(None)

def test_boolean_input():
    result = car_race_collision(True)
    assert result == 1  # True is treated as 1