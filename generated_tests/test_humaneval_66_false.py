# Test cases for HumanEval/66
# Generated using Claude API


def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """

    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)


# Generated test cases:
import pytest

@pytest.mark.parametrize("input_str,expected", [
    ("", 0),
    ("a", 0),
    ("A", 65),
    ("ABC", 198),
    ("aBcDeF", 204),
    ("abcdef", 0),
    ("HELLO", 372),
    ("Hello World", 159),
    ("123", 0),
    ("A1B2C3", 198),
    ("!@#$%", 0),
    ("Mixed123UPPER", 473),
    ("     ", 0),
    ("SPACES   IN   TEXT", 923),
    ("ПриветHELLO", 372),
])
def test_digit_sum(input_str, expected):
    if not isinstance(input_str, str):
        with pytest.raises(TypeError):
            digitSum(input_str)
        return
    assert digitSum(input_str) == expected

def test_digit_sum_with_none():
    with pytest.raises(AttributeError):
        digitSum(None)

def test_digit_sum_with_non_string():
    with pytest.raises(AttributeError):
        digitSum(123)

def test_digit_sum_with_boolean():
    with pytest.raises(AttributeError):
        digitSum(True)

def test_digit_sum_with_list():
    with pytest.raises(AttributeError):
        digitSum(['A', 'B', 'C'])

def test_digit_sum_with_special_chars():
    assert digitSum("!@#$%^&*()_+") == 0

def test_digit_sum_all_lowercase():
    assert digitSum("abcdefghijklmnopqrstuvwxyz") == 0

def test_digit_sum_all_uppercase():
    assert digitSum("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 2015