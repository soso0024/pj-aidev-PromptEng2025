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
from typing import Optional

def test_decode_shift_basic():
    assert decode_shift("mjqqt") == "hello"
    assert decode_shift("kfhj") == "face"

@pytest.mark.parametrize("input_str,expected", [
    ("", ""),
    ("a", "v"),
    ("z", "u"),
    ("abcde", "vwxyz"),
    ("zzzzz", "uuuuu"),
    ("mjqqt btwqi", "hello world"),
    ("ymfy nx fs jcfruqj", "that is an example")
])
def test_decode_shift_parametrized(input_str: str, expected: str):
    result = decode_shift(input_str)
    assert result == expected

def test_decode_shift_roundtrip():
    original = "thisisateststring"
    encoded = encode_shift(original)
    decoded = decode_shift(encoded)
    assert decoded == original

def test_decode_shift_multiple_rounds():
    text = "testtext"
    for _ in range(5):
        encoded = encode_shift(text)
        decoded = decode_shift(encoded)
        assert decoded == text

@pytest.mark.parametrize("input_str", [
    "Hello",
    "123",
    "!@#",
    "Hello World 123!"
])
def test_decode_shift_invalid_input(input_str):
    try:
        result = decode_shift(input_str.lower())
        assert all(c.isalpha() or c.isspace() for c in result)
    except Exception:
        pass

def test_decode_shift_long_string():
    long_input = "a" * 1000
    expected = "v" * 1000
    assert decode_shift(long_input) == expected

def test_decode_shift_repeated_chars():
    assert decode_shift("aaaaa") == "vvvvv"
    assert decode_shift("zzzzz") == "uuuuu"

def test_decode_shift_alphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded = decode_shift(encode_shift(alphabet))
    assert decoded == alphabet