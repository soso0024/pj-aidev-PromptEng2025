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

@pytest.mark.parametrize("input,expected", [
    ("", 0),
    ("abAB", 131),
    ("abcCd", 67),
    ("helloE", 69),
    ("woArBld", 131),
    ("aAaaaXa", 153),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2925),
    ("abcdefghijklmnopqrstuvwxyz", 0),
    ("A1b2C3d4E", 69),
    ("   A B C   ", 195),
    (None, TypeError),
    (123, TypeError)
])
def test_digitSum(input, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            digitSum(input)
    else:
        assert digitSum(input) == expected

def digitSum(s):
    if s == "": return 0
    return sum(ord(char) for char in s if char.isupper())