# Test cases for HumanEval/2
# Generated using Claude API



def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    return number % 1.0


# Generated test cases:
import pytest
import math

def truncate_number(number: float):
    return number % 1.0

class TestTruncateNumber:
    
    def test_positive_decimal(self):
        assert truncate_number(3.5) == 0.5
        assert truncate_number(1.25) == 0.25
        assert abs(truncate_number(7.999) - 0.999) < 1e-10
    
    def test_negative_decimal(self):
        assert truncate_number(-3.5) == 0.5
        assert truncate_number(-1.25) == 0.75
        assert abs(truncate_number(-7.999) - 0.001) < 1e-10
    
    def test_whole_numbers(self):
        assert truncate_number(5.0) == 0.0
        assert truncate_number(-5.0) == 0.0
        assert truncate_number(0.0) == 0.0
        assert truncate_number(1.0) == 0.0
        assert truncate_number(-1.0) == 0.0
    
    def test_integers(self):
        assert truncate_number(5) == 0.0
        assert truncate_number(-5) == 0.0
        assert truncate_number(0) == 0.0
        assert truncate_number(1) == 0.0
        assert truncate_number(-1) == 0.0
    
    def test_small_decimals(self):
        assert truncate_number(0.1) == 0.1
        assert truncate_number(0.01) == 0.01
        assert truncate_number(0.001) == 0.001
        assert truncate_number(-0.1) == 0.9
        assert truncate_number(-0.01) == 0.99
    
    def test_large_numbers(self):
        assert truncate_number(1000.5) == 0.5
        assert truncate_number(-1000.5) == 0.5
        assert abs(truncate_number(999999.123) - 0.123) < 1e-10
        assert abs(truncate_number(-999999.123) - 0.877) < 1e-10
    
    def test_very_small_positive_decimals(self):
        result = truncate_number(0.0001)
        assert abs(result - 0.0001) < 1e-10
    
    def test_very_small_negative_decimals(self):
        result = truncate_number(-0.0001)
        assert abs(result - 0.9999) < 1e-10
    
    def test_floating_point_precision(self):
        result = truncate_number(1.0000000001)
        assert result > 0
        assert result < 1
    
    @pytest.mark.parametrize("input_val,expected", [
        (3.14, 0.14),
        (2.71, 0.71),
        (10.0, 0.0),
        (-2.5, 0.5),
        (-10.0, 0.0),
        (0.999, 0.999),
        (-0.999, 0.001)
    ])
    def test_parametrized_cases(self, input_val, expected):
        result = truncate_number(input_val)
        assert abs(result - expected) < 1e-10
    
    def test_special_float_values(self):
        result_inf = truncate_number(float('inf'))
        assert math.isnan(result_inf)
        
        result_neg_inf = truncate_number(float('-inf'))
        assert math.isnan(result_neg_inf)
        
        result_nan = truncate_number(float('nan'))
        assert math.isnan(result_nan)
    
    def test_type_errors(self):
        with pytest.raises(TypeError):
            truncate_number("string")
        
        with pytest.raises(TypeError):
            truncate_number(None)
        
        with pytest.raises(TypeError):
            truncate_number([1, 2, 3])
        
        with pytest.raises(TypeError):
            truncate_number({"key": "value"})
    
    def test_return_type(self):
        result = truncate_number(3.5)
        assert isinstance(result, float)
        
        result = truncate_number(5)
        assert isinstance(result, float)
    
    def test_boundary_values(self):
        assert truncate_number(0.999999999) < 1.0
        assert truncate_number(0.999999999) > 0.0
        assert truncate_number(-0.000000001) < 1.0
        assert truncate_number(-0.000000001) > 0.0