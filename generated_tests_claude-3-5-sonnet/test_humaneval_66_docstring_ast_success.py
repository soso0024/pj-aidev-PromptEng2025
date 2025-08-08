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
    ("abAB", 131),
    ("abcCd", 67),
    ("helloE", 69),
    ("woArBld", 131),
    ("aAaaaXa", 153),
    ("a", 0),
    ("A", 65),
    ("Z", 90),
    ("aAbBcC", 198),
    ("123ABC", 198),
    ("!@#$%^", 0),
    ("Mixed123CASES", 444),
    ("ALL_CAPS", 512),
    ("no_caps", 0),
])
def test_digit_sum(input_str, expected):
    assert digitSum(input_str) == expected

def test_digit_sum_with_special_chars():
    assert digitSum("A!B@C#") == 198

def test_digit_sum_with_spaces():
    assert digitSum("A B C") == 198

def test_digit_sum_with_numbers():
    assert digitSum("A1B2C3") == 198

def test_digit_sum_with_unicode():
    assert digitSum("ABC") == 198

def test_digit_sum_with_newlines():
    assert digitSum("A\nB\nC") == 198

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    True,
    3.14
])
def test_digit_sum_invalid_input(invalid_input):
    with pytest.raises((AttributeError, TypeError)):
        digitSum(invalid_input)