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
from your_module import digitSum

@pytest.mark.parametrize("input_str, expected", [
    ("", 0),
    ("abAB", 131),
    ("abcCd", 67),
    ("helloE", 69),
    ("woArBld", 131),
    ("aAaaaXa", 153),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2925),
    ("abcdefghijklmnopqrstuvwxyz", 0),
    ("123456789", 0),
    ("!@#$%^&*()_+", 0),
])
def test_digitSum(input_str, expected):
    assert digitSum(input_str) == expected

def test_digitSum_empty_string():
    assert digitSum("") == 0

def test_digitSum_all_uppercase():
    assert digitSum("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 2925

def test_digitSum_all_lowercase():
    assert digitSum("abcdefghijklmnopqrstuvwxyz") == 0

def test_digitSum_all_numbers():
    assert digitSum("123456789") == 0

def test_digitSum_all_special_characters():
    assert digitSum("!@#$%^&*()_+") == 0