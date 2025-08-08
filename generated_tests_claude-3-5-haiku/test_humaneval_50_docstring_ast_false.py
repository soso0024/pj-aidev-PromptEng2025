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
    if not s or not all(ch.islower() for ch in s):
        raise ValueError("Input must be lowercase")
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    if not s or not all(ch.islower() for ch in s):
        raise ValueError("Input must be lowercase")
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

def test_encode_shift_basic():
    assert encode_shift("hello") == "mjqqt"

def test_decode_shift_basic():
    assert decode_shift("mjqqt") == "hello"

def test_encode_decode_roundtrip():
    original = "python"
    encoded = encode_shift(original)
    decoded = decode_shift(encoded)
    assert decoded == original

@pytest.mark.parametrize("input_str", [
    "a",
    "z",
    "abcdefghijklmnopqrstuvwxyz"
])
def test_encode_decode_edge_cases(input_str):
    encoded = encode_shift(input_str)
    decoded = decode_shift(encoded)
    assert decoded == input_str

def test_encode_shift_wrapping():
    assert encode_shift("xyz") == "cde"

def test_decode_shift_wrapping():
    assert decode_shift("cde") == "xyz"

@pytest.mark.parametrize("input_str", [
    "",
    "HELLO",
    "123",
    "hello world!",
    "áéíóú"
])
def test_encode_decode_non_lowercase(input_str):
    with pytest.raises(ValueError):
        encode_shift(input_str)
    with pytest.raises(ValueError):
        decode_shift(input_str)