# Test cases for HumanEval/65
# Generated using Claude API


def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


# Generated test cases:
import pytest

def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

class TestCircularShift:
    
    def test_zero_shift(self):
        assert circular_shift(12345, 0) == "12345"
        assert circular_shift(0, 0) == "0"
        assert circular_shift(999, 0) == "999"
    
    def test_shift_less_than_length(self):
        assert circular_shift(12345, 1) == "51234"
        assert circular_shift(12345, 2) == "45123"
        assert circular_shift(12345, 3) == "34512"
        assert circular_shift(12345, 4) == "23451"
        assert circular_shift(12345, 5) == "12345"
    
    def test_shift_equal_to_length(self):
        assert circular_shift(123, 3) == "123"
        assert circular_shift(1, 1) == "1"
        assert circular_shift(99, 2) == "99"
    
    def test_shift_greater_than_length(self):
        assert circular_shift(123, 4) == "321"
        assert circular_shift(12345, 6) == "54321"
        assert circular_shift(1, 5) == "1"
        assert circular_shift(99, 10) == "99"
    
    def test_single_digit(self):
        assert circular_shift(5, 0) == "5"
        assert circular_shift(5, 1) == "5"
        assert circular_shift(5, 2) == "5"
    
    def test_negative_numbers(self):
        assert circular_shift(-123, 1) == "3-12"
        assert circular_shift(-123, 2) == "23-1"
        assert circular_shift(-123, 5) == "321-"
    
    def test_large_shift_values(self):
        assert circular_shift(123, 100) == "321"
        assert circular_shift(12345, 1000) == "54321"
    
    @pytest.mark.parametrize("x,shift,expected", [
        (12345, 1, "51234"),
        (12345, 2, "45123"),
        (123, 4, "321"),
        (0, 0, "0"),
        (0, 5, "0"),
        (7, 1, "7"),
        (789, 0, "789"),
        (789, 3, "789"),
        (-456, 1, "6-45"),
        (-456, 10, "654-")
    ])
    def test_parametrized_cases(self, x, shift, expected):
        assert circular_shift(x, shift) == expected
    
    def test_float_input(self):
        assert circular_shift(12.34, 1) == "412.3"
        assert circular_shift(12.34, 6) == "43.21"
    
    def test_boolean_input(self):
        assert circular_shift(True, 1) == "eTru"
        assert circular_shift(False, 2) == "seFal"
        assert circular_shift(True, 10) == "eurT"