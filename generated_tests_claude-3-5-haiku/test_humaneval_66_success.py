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

def test_digitSum_empty_string():
    assert digitSum("") == 0

def test_digitSum_no_uppercase():
    assert digitSum("hello") == 0

def test_digitSum_all_uppercase():
    assert digitSum("HELLO") == 372

def test_digitSum_mixed_case():
    assert digitSum("HeLLo") == 224

def test_digitSum_with_numbers():
    assert digitSum("H3llo") == 72

def test_digitSum_with_special_chars():
    assert digitSum("H3llo!") == 72

@pytest.mark.parametrize("input_str,expected", [
    ("", 0),
    ("hello", 0),
    ("HELLO", 372),
    ("HeLLo", 224),
    ("H3llo", 72),
    ("H3llo!", 72),
    ("PYTHON", 482),
    ("Python", 80)
])
def test_digitSum_parametrized(input_str, expected):
    assert digitSum(input_str) == expected