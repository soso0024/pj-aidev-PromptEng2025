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

def test_zero_input():
    assert car_race_collision(0) == 0

def test_positive_numbers():
    assert car_race_collision(1) == 1
    assert car_race_collision(2) == 4
    assert car_race_collision(5) == 25
    assert car_race_collision(10) == 100

def test_negative_numbers():
    with pytest.raises(ValueError):
        car_race_collision(-1)
    with pytest.raises(ValueError):
        car_race_collision(-2)
    with pytest.raises(ValueError):
        car_race_collision(-5)

@pytest.mark.parametrize("input_n,expected", [
    (0, 0),
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25)
])
def test_parametrized_inputs(input_n, expected):
    assert car_race_collision(input_n) == expected

def test_large_numbers():
    assert car_race_collision(100) == 10000
    assert car_race_collision(1000) == 1000000

@pytest.mark.parametrize("invalid_input", [
    "string",
    None,
    [],
    {},
])
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        car_race_collision(invalid_input)

def test_float_and_complex():
    assert car_race_collision(1.0) == 1
    assert car_race_collision(2.0) == 4
    with pytest.raises(TypeError):
        car_race_collision(1.5)
    with pytest.raises(TypeError):
        car_race_collision(complex(1, 2))