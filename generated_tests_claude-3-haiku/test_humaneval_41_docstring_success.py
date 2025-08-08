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

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 4),
    (3, 9),
    (10, 100),
    (-1, ValueError),
    (3.14, ValueError),
    ('3', ValueError)
])
def test_car_race_collision(n, expected):
    if expected == ValueError:
        with pytest.raises(expected):
            car_race_collision(n)
    else:
        assert car_race_collision(n) == expected

def car_race_collision(n: int):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    return n**2