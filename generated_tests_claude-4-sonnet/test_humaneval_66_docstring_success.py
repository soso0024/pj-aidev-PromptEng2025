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

def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

@pytest.mark.parametrize("input_str,expected", [
    ("", 0),
    ("abAB", 131),
    ("abcCd", 67),
    ("helloE", 69),
    ("woArBld", 131),
    ("aAaaaXa", 153),
    ("abc", 0),
    ("ABC", 198),
    ("A", 65),
    ("Z", 90),
    ("aZ", 90),
    ("Za", 90),
    ("AaAaAa", 195),
    ("123ABC", 198),
    ("!@#ABC", 198),
    ("   ABC   ", 198),
    ("AbCdEfG", 65 + 67 + 69 + 71),
    ("lowercase", 0),
    ("UPPERCASE", 85 + 80 + 80 + 69 + 82 + 67 + 65 + 83 + 69),
    ("MiXeD", 77 + 88 + 68),
    ("123", 0),
    ("!@#$%", 0),
    ("   ", 0),
    ("\n\t", 0),
    ("A\nB\tC", 65 + 66 + 67),
])
def test_digitSum(input_str, expected):
    assert digitSum(input_str) == expected

def test_digitSum_single_uppercase():
    for i in range(65, 91):
        char = chr(i)
        assert digitSum(char) == i

def test_digitSum_single_lowercase():
    for i in range(97, 123):
        char = chr(i)
        assert digitSum(char) == 0

def test_digitSum_mixed_case_long_string():
    s = "AbCdEfGhIjKlMnOpQrStUvWxYz"
    expected = sum(ord(c) for c in s if c.isupper())
    assert digitSum(s) == expected

def test_digitSum_only_special_characters():
    assert digitSum("!@#$%^&*()") == 0

def test_digitSum_numbers_and_uppercase():
    assert digitSum("123ABC456") == 65 + 66 + 67

def test_digitSum_whitespace_and_uppercase():
    assert digitSum(" A B C ") == 65 + 66 + 67