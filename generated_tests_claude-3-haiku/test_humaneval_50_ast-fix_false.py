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
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

def test_decode_shift_empty_string():
    assert decode_shift("") == ""

@pytest.mark.parametrize("input,expected", [
    ("hello", "czggj"),
    ("world", "tloia"),
    ("python", "ktvmlk"),
    ("abcdefghijklmnopqrstuvwxyz", "vwxyzabcdefghijklmnopqrstu")
])
def test_decode_shift_normal_cases(input, expected):
    assert decode_shift(input) == expected

def test_decode_shift_non_alphabetic_characters():
    assert decode_shift("hello123!@#") == "czggj123!@#"

def test_decode_shift_uppercase_characters():
    assert decode_shift("HELLO") == "CZGGJ"

def test_decode_shift_mixed_case():
    assert decode_shift("Hello World") == "Czggj Tloia"

def test_decode_shift_non_ascii_characters():
    assert decode_shift("héllò wórld") == "ébggò xñogf"

def test_decode_shift_raises_type_error():
    with pytest.raises(TypeError):
        decode_shift(123)