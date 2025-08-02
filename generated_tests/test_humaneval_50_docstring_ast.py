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
    assert decode_shift("yfhj") == "tace"

def test_decode_shift_empty():
    assert decode_shift("") == ""

def test_decode_shift_single_char():
    assert decode_shift("f") == "a"
    assert decode_shift("z") == "u"

@pytest.mark.parametrize("encoded,decoded", [
    ("mjqqt", "hello"),
    ("yfhj", "tace"),
    ("yttq", "tool"),
    ("yjxy", "test"),
    ("uwtlwfr", "program"),
])
def test_decode_shift_various_words(encoded, decoded):
    assert decode_shift(encoded) == decoded

def test_decode_shift_wrapping():
    assert decode_shift("z") == "u"
    assert decode_shift("a") == "v"
    assert decode_shift("b") == "w"

def test_decode_shift_long_text():
    assert decode_shift("ymjvznhpgwtbsktcozruxtajwymjqfeditl") == "thequickbrownfoxjumpsoverthelazydog"

@pytest.mark.parametrize("original", [
    "hello",
    "python",
    "programming",
    "test",
    "abcdefghijklmnopqrstuvwxyz"
])
def test_encode_decode_roundtrip(original):
    encoded = encode_shift(original)
    decoded = decode_shift(encoded)
    assert decoded == original

def test_decode_shift_repeated_chars():
    assert decode_shift("ffff") == "aaaa"
    assert decode_shift("zzzz") == "uuuu"

def test_decode_shift_alternating_chars():
    assert decode_shift("fgfgfg") == "ababab"

def test_decode_shift_invalid_input():
    for invalid_input in ["ABC", "123", "!@#", "Hello World", "Mixed123Case"]:
        try:
            decode_shift(invalid_input.lower())
        except ValueError:
            pass