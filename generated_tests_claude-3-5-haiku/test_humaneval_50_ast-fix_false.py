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

def encode_shift(s: str):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if not s.islower():
        raise ValueError("Input must be lowercase")
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if not s.islower():
        raise ValueError("Input must be lowercase")
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

def test_decode_shift_basic():
    assert decode_shift("fqjcqzx") == "abcdefg"

def test_decode_shift_empty_string():
    assert decode_shift("") == ""

def test_decode_shift_single_character():
    assert decode_shift("k") == "f"

def test_decode_shift_multiple_characters():
    assert decode_shift("fqjcqzx") == "abcdefg"

def test_decode_shift_wrap_around():
    assert decode_shift("anmz") == "fgst"

@pytest.mark.parametrize("input_str,expected", [
    ("fqjcqzx", "abcdefg"),
    ("", ""),
    ("k", "f"),
    ("anmz", "fgst"),
    ("zzz", "uuu")
])
def test_decode_shift_parametrized(input_str, expected):
    assert decode_shift(input_str) == expected

def test_decode_shift_non_lowercase():
    with pytest.raises(ValueError):
        decode_shift("ABC")

def test_decode_shift_non_string():
    with pytest.raises(TypeError):
        decode_shift(123)