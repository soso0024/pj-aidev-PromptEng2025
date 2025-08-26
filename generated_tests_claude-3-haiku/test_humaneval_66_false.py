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

def test_digitSum_all_uppercase():
    assert digitSum("ABCD") == 266

def test_digitSum_all_lowercase():
    assert digitSum("abcd") == 0

def test_digitSum_mixed_case():
    assert digitSum("Aa1Bb2Cc3") == 198

def test_digitSum_non_alphabetic_characters():
    assert digitSum("123!@#") == 66

@pytest.mark.parametrize("input,expected", [
    ("", 0),
    ("ABCD", 266),
    ("abcd", 0),
    ("Aa1Bb2Cc3", 198),
    ("123!@#", 66)
])
def test_digitSum_parametrized(input, expected):
    assert digitSum(input) == expected

def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)