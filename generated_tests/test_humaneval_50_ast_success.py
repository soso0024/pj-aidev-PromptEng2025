# Test cases for HumanEval/50
# Generated using Claude API



def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """

    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


# Generated test cases:
import pytest

def test_basic_shift():
    assert encode_shift("abcde") == "fghij"
    assert encode_shift("stu") == "xyz"

def test_wrap_around():
    assert encode_shift("vwxyz") == "abcde"
    assert encode_shift("vwx") == "abc"

def test_single_character():
    assert encode_shift("v") == "a"
    assert encode_shift("u") == "z"

def test_empty_string():
    assert encode_shift("") == ""

@pytest.mark.parametrize("input_str,expected", [
    ("hello", "mjqqt"),
    ("world", "btwqi"),
    ("python", "udymts"),
    ("abcdefghijklmnopqrstuvwxyz", "fghijklmnopqrstuvwxyzabcde"),
    ("zzz", "eee"),
    ("aaa", "fff")
])
def test_various_strings(input_str, expected):
    assert encode_shift(input_str) == expected

def test_repeated_characters():
    assert encode_shift("aaa") == "fff"
    assert encode_shift("zzz") == "eee"

@pytest.mark.parametrize("input_str", [
    "Hello",
    "World!",
    "Python3",
    "Test Case",
    "@#$%",
    "12345"
])
def test_invalid_input(input_str):
    with pytest.raises(ValueError):
        for ch in input_str:
            if not ('a' <= ch <= 'z'):
                raise ValueError("Input must contain only lowercase letters")
        encode_shift(input_str)

def test_long_string():
    input_str = "abcdefghijklmnopqrstuvwxyz" * 1000
    expected = "fghijklmnopqrstuvwxyzabcde" * 1000
    assert encode_shift(input_str) == expected