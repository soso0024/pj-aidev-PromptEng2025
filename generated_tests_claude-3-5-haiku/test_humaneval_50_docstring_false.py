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

def test_encode_shift_basic():
    assert encode_shift("hello") == "mjqqt"

def test_encode_shift_empty_string():
    assert encode_shift("") == ""

def test_encode_shift_full_alphabet():
    assert encode_shift("abcdefghijklmnopqrstuvwxyz") == "fghijklmnopqrstuvwxyzabcde"

def test_decode_shift_basic():
    assert decode_shift("mjqqt") == "hello"

def test_decode_shift_empty_string():
    assert decode_shift("") == ""

def test_decode_shift_full_alphabet():
    assert decode_shift("fghijklmnopqrstuvwxyzabcde") == "abcdefghijklmnopqrstuvwxyz"

@pytest.mark.parametrize("input_str,expected", [
    ("hello", "mjqqt"),
    ("world", "btwqi"),
    ("python", "udymore"),
    ("", ""),
    ("a", "f"),
    ("z", "e")
])
def test_encode_shift_parametrized(input_str, expected):
    assert encode_shift(input_str) == expected

@pytest.mark.parametrize("input_str,expected", [
    ("mjqqt", "hello"),
    ("btwqi", "world"),
    ("udymore", "python"),
    ("", ""),
    ("f", "a"),
    ("e", "z")
])
def test_decode_shift_parametrized(input_str, expected):
    assert decode_shift(input_str) == expected

def test_encode_decode_roundtrip():
    original = "helloworld"
    encoded = encode_shift(original)
    decoded = decode_shift(encoded)
    assert decoded == original