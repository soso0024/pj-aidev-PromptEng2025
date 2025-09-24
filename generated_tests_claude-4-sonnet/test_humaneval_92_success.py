# Test cases for HumanEval/92
# Generated using Claude API


def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''

    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False


# Generated test cases:
import pytest

def any_int(x, y, z):
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False

class TestAnyInt:
    
    def test_all_integers_sum_condition_true_case1(self):
        assert any_int(1, 2, 3) == True
    
    def test_all_integers_sum_condition_true_case2(self):
        assert any_int(3, 1, 2) == True
    
    def test_all_integers_sum_condition_true_case3(self):
        assert any_int(2, 3, 1) == True
    
    def test_all_integers_sum_condition_false(self):
        assert any_int(1, 2, 4) == False
    
    def test_negative_integers_sum_true(self):
        assert any_int(-1, -2, -3) == True
    
    def test_negative_integers_sum_false(self):
        assert any_int(-1, -2, -5) == False
    
    def test_mixed_positive_negative_sum_true(self):
        assert any_int(-1, 2, 1) == True
    
    def test_mixed_positive_negative_sum_false(self):
        assert any_int(-1, 2, 5) == False
    
    def test_zero_values_sum_true(self):
        assert any_int(0, 0, 0) == True
    
    def test_zero_with_other_values_sum_true(self):
        assert any_int(0, 1, 1) == True
    
    def test_zero_with_other_values_sum_false(self):
        assert any_int(0, 1, 3) == False
    
    def test_large_integers_sum_true(self):
        assert any_int(1000, 2000, 3000) == True
    
    def test_large_integers_sum_false(self):
        assert any_int(1000, 2000, 5000) == False
    
    def test_one_float_parameter(self):
        assert any_int(1.0, 2, 3) == False
    
    def test_two_float_parameters(self):
        assert any_int(1.0, 2.0, 3) == False
    
    def test_all_float_parameters(self):
        assert any_int(1.0, 2.0, 3.0) == False
    
    def test_one_string_parameter(self):
        assert any_int("1", 2, 3) == False
    
    def test_all_string_parameters(self):
        assert any_int("1", "2", "3") == False
    
    def test_none_parameters(self):
        assert any_int(None, None, None) == False
    
    def test_mixed_types_with_none(self):
        assert any_int(1, None, 3) == False
    
    def test_boolean_parameters(self):
        assert any_int(True, False, True) == True
    
    def test_list_parameters(self):
        assert any_int([1], [2], [3]) == False
    
    def test_empty_string_parameters(self):
        assert any_int("", "", "") == False
    
    @pytest.mark.parametrize("x,y,z,expected", [
        (1, 1, 2, True),
        (2, 1, 1, True),
        (1, 2, 1, True),
        (5, 3, 8, True),
        (8, 3, 5, True),
        (3, 8, 5, True),
        (1, 1, 1, False),
        (1, 2, 5, False),
        (10, 20, 50, False)
    ])
    def test_parametrized_integer_cases(self, x, y, z, expected):
        assert any_int(x, y, z) == expected
    
    @pytest.mark.parametrize("x,y,z", [
        (1.5, 2, 3),
        (1, 2.5, 3),
        (1, 2, 3.5),
        ("a", "b", "c"),
        ([], {}, set()),
        (complex(1,2), 2, 3)
    ])
    def test_parametrized_non_integer_cases(self, x, y, z):
        assert any_int(x, y, z) == False