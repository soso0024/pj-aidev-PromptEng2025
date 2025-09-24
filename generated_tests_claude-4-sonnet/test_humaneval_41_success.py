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
    return n**2

class TestCarRaceCollision:
    
    def test_zero_cars(self):
        assert car_race_collision(0) == 0
    
    def test_one_car(self):
        assert car_race_collision(1) == 1
    
    def test_two_cars(self):
        assert car_race_collision(2) == 4
    
    def test_three_cars(self):
        assert car_race_collision(3) == 9
    
    @pytest.mark.parametrize("n,expected", [
        (4, 16),
        (5, 25),
        (10, 100),
        (100, 10000),
        (1000, 1000000)
    ])
    def test_positive_integers(self, n, expected):
        assert car_race_collision(n) == expected
    
    def test_negative_number(self):
        assert car_race_collision(-1) == 1
        assert car_race_collision(-2) == 4
        assert car_race_collision(-5) == 25
    
    @pytest.mark.parametrize("n,expected", [
        (-3, 9),
        (-10, 100),
        (-100, 10000)
    ])
    def test_negative_numbers_parametrized(self, n, expected):
        assert car_race_collision(n) == expected
    
    def test_large_numbers(self):
        assert car_race_collision(999) == 998001
        assert car_race_collision(1001) == 1002001
    
    def test_float_input(self):
        assert car_race_collision(5.0) == 25.0
        assert car_race_collision(3.0) == 9.0
    
    def test_type_error_string(self):
        with pytest.raises(TypeError):
            car_race_collision("5")
    
    def test_type_error_none(self):
        with pytest.raises(TypeError):
            car_race_collision(None)
    
    def test_type_error_list(self):
        with pytest.raises(TypeError):
            car_race_collision([5])
    
    def test_type_error_dict(self):
        with pytest.raises(TypeError):
            car_race_collision({"n": 5})