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
    assert digitSum("abc") == 0

def test_digitSum_all_uppercase():
    assert digitSum("ABC") == 198

def test_digitSum_mixed_case():
    assert digitSum("abAB") == 131

def test_digitSum_single_uppercase():
    assert digitSum("hello") == 0
    assert digitSum("helloE") == 69

def test_digitSum_multiple_uppercase():
    assert digitSum("woArBld") == 131

def test_digitSum_repeated_uppercase():
    assert digitSum("aAaaaXa") == 153

@pytest.mark.parametrize("input_str,expected", [
    ("", 0),
    ("abc", 0),
    ("ABC", 198),
    ("abAB", 131),
    ("helloE", 69),
    ("woArBld", 131),
    ("aAaaaXa", 153),
    ("HELLO WORLD", 520),
    ("123ABCdef", 198)
])
def test_digitSum_parametrized(input_str, expected):
    assert digitSum(input_str) == expected