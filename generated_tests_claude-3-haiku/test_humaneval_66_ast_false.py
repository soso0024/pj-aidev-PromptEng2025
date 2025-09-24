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
    return sum(ord(char) for char in s if char.isupper())

def test_digitSum_empty_string():
    assert digitSum("") == 0

@pytest.mark.parametrize("input,expected", [
    ("ABC123DEF", 66),
    ("a1c2e3g4i5", 0),
    ("PYTHON", 80),
    ("H3LL0 W0RLD", 66),
    ("1234567890", 0)
])
def test_digitSum_valid_inputs(input, expected):
    assert digitSum(input) == expected

def test_digitSum_non_string_input():
    with pytest.raises(TypeError):
        digitSum(123)