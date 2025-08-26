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
    assert digitSum("abcd") == 0

def test_digitSum_all_uppercase():
    assert digitSum("ABCD") == 266

def test_digitSum_mixed_case():
    assert digitSum("abAB") == 131

def test_digitSum_complex_case():
    assert digitSum("woArBld") == 131

def test_digitSum_multiple_uppercase():
    assert digitSum("aAaaaXa") == 153

@pytest.mark.parametrize("input_str,expected", [
    ("", 0),
    ("abcCd", 67),
    ("helloE", 69),
    ("PYTHON", 482),
    ("pythonPROGRAMMING", 835),
    ("a1B2c3D4", 134)
])
def test_digitSum_parametrized(input_str, expected):
    assert digitSum(input_str) == expected