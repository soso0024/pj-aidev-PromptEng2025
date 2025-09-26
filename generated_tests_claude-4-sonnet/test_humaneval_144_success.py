# Test cases for HumanEval/144
# Generated using Claude API


def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False


# Generated test cases:
import pytest

def simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False

class TestSimplify:
    
    @pytest.mark.parametrize("x,n,expected", [
        ("1/5", "5/1", True),
        ("1/6", "2/1", False),
        ("7/10", "10/2", False),
        ("2/6", "5/2", False),
        ("4/6", "7/5", False),
        ("1/1", "1/1", True),
        ("2/4", "8/4", True),
        ("3/7", "14/6", True),
        ("1/2", "3/4", False),
        ("5/8", "8/5", True),
        ("0/1", "1/1", True),
        ("0/5", "3/2", True),
        ("1/3", "0/1", True),
        ("10/20", "4/2", True),
        ("15/25", "5/3", True),
        ("100/200", "2/1", True),
        ("1/1000", "1000/1", True),
        ("999/1000", "1000/999", True),
        ("13/17", "17/13", True),
        ("11/13", "26/22", True)
    ])
    def test_simplify_parametrized(self, x, n, expected):
        assert simplify(x, n) == expected
    
    def test_simplify_basic_true_cases(self):
        assert simplify("1/5", "5/1") == True
        assert simplify("7/10", "10/2") == False
        assert simplify("2/4", "8/4") == True
        
    def test_simplify_basic_false_cases(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("2/6", "5/2") == False
        assert simplify("1/2", "3/4") == False
        
    def test_simplify_with_zero_numerator(self):
        assert simplify("0/1", "1/1") == True
        assert simplify("0/5", "3/2") == True
        assert simplify("0/100", "999/1") == True
        
    def test_simplify_with_zero_in_second_fraction(self):
        assert simplify("1/3", "0/1") == True
        assert simplify("5/7", "0/2") == True
        
    def test_simplify_identical_fractions(self):
        assert simplify("1/1", "1/1") == True
        assert simplify("2/3", "3/2") == True
        assert simplify("5/7", "7/5") == True
        
    def test_simplify_large_numbers(self):
        assert simplify("100/200", "200/100") == True
        assert simplify("1000/2000", "3000/1500") == True
        assert simplify("999/1001", "1001/999") == True
        
    def test_simplify_unit_fractions(self):
        assert simplify("1/2", "2/1") == True
        assert simplify("1/3", "3/1") == True
        assert simplify("1/7", "7/1") == True
        
    def test_simplify_negative_results(self):
        assert simplify("1/4", "2/3") == False
        assert simplify("3/8", "5/7") == False
        assert simplify("11/13", "17/19") == False

    def test_division_by_zero_error(self):
        with pytest.raises(ZeroDivisionError):
            simplify("1/0", "2/3")
        with pytest.raises(ZeroDivisionError):
            simplify("2/3", "1/0")
        with pytest.raises(ZeroDivisionError):
            simplify("1/0", "1/0")
            
    def test_invalid_format_error(self):
        with pytest.raises(ValueError):
            simplify("1", "2/3")
        with pytest.raises(ValueError):
            simplify("1/2", "3")
        with pytest.raises(ValueError):
            simplify("a/b", "1/2")
        with pytest.raises(ValueError):
            simplify("1/2", "c/d")