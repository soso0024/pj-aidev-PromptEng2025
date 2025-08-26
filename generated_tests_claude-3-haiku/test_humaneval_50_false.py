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
from your_module import decode_shift

@pytest.mark.parametrize("input_str, expected", [
    ("hello", "ebccm"),
    ("world", "tmqjb"),
    ("python", "ktvipp"),
    ("", ""),
    ("a", "r"),
    ("z", "u"),
    ("abc", "xyz"),
    ("ABC", "XYZ"),
    ("123", "023"),
    ("hello world", "ebccm tmqjb"),
    ("HELLO WORLD", "EBCCM TMQJB"),
    ("HeLlO wOrLd", "EbCcM TmQjB"),
])
def test_decode_shift(input_str, expected):
    assert decode_shift(input_str) == expected

def test_decode_shift_non_string():
    with pytest.raises(TypeError):
        decode_shift(123)

def test_decode_shift_none():
    with pytest.raises(TypeError):
        decode_shift(None)