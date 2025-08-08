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

def test_decode_shift_empty_string():
    assert decode_shift("") == ""

@pytest.mark.parametrize("input_str,expected", [
    ("hello", "czggj"),
    ("world", "rjmgy"),
    ("python", "ktocji"),
    ("abcdefghijklmnopqrstuvwxyz", "vwxyzabcdefghijklmnopqrstu")
])
def test_decode_shift_normal_cases(input_str, expected):
    assert decode_shift(input_str) == expected

def test_decode_shift_non_alphabetic_characters():
    assert decode_shift("hello123!@#") == "czggjzabjol"

def test_decode_shift_uppercase_characters():
    assert decode_shift("HELLO") == "wtaad"

def test_decode_shift_mixed_case_characters():
    assert decode_shift("Hello World") == "wzggjiljmgy"

def test_decode_shift_single_character():
    assert decode_shift("a") == "v"
    assert decode_shift("z") == "u"

def test_decode_shift_invalid_input():
    with pytest.raises(TypeError):
        decode_shift(123)