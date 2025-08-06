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

def test_empty_string():
    assert digitSum("") == 0

def test_no_uppercase():
    assert digitSum("hello") == 0

def test_single_uppercase():
    assert digitSum("Hello") == 72

def test_all_uppercase():
    assert digitSum("HELLO") == 372

def test_mixed_case():
    assert digitSum("HeLLo") == 224

@pytest.mark.parametrize("input_str,expected", [
    ("ABC", 198),
    ("abc", 0),
    ("A1B2C3", 198),
    ("aA bB cC", 198),
    ("!@#$%", 0),
    ("TEST123", 320),
    ("", 0),
    ("  ", 0),
    ("Z", 90),
    ("Mixed WITH Capitals", 460)
])
def test_various_inputs(input_str, expected):
    assert digitSum(input_str) == expected

def test_special_characters():
    assert digitSum("Hello!@#$%^&*()") == 72

def test_numbers():
    assert digitSum("123ABC123") == 198

def test_whitespace():
    assert digitSum("  A  B  C  ") == 198

def test_unicode_letters():
    assert digitSum("A") == 65

def test_long_string():
    assert digitSum("A" * 1000) == 65 * 1000

def test_newlines():
    assert digitSum("A\nB\nC") == 198