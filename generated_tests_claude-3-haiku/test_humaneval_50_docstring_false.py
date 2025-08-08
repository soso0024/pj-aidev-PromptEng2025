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
from encode_shift import encode_shift
from decode_shift import decode_shift

def test_encode_shift_empty_string():
    assert encode_shift("") == ""

def test_encode_shift_lowercase_letters():
    assert encode_shift("abcxyz") == "fghcde"

def test_encode_shift_uppercase_letters():
    assert encode_shift("ABCXYZ") == "FGHCDE"

def test_encode_shift_mixed_case():
    assert encode_shift("aBcXyZ") == "fGhCdE"

def test_encode_shift_non_alphabetic_characters():
    assert encode_shift("abc123!@#") == "fgh123!@#"

def test_decode_shift_empty_string():
    assert decode_shift("") == ""

def test_decode_shift_lowercase_letters():
    assert decode_shift("fghcde") == "abcxyz"

def test_decode_shift_uppercase_letters():
    assert decode_shift("FGHCDE") == "ABCXYZ"

def test_decode_shift_mixed_case():
    assert decode_shift("fGhCdE") == "aBcXyZ"

def test_decode_shift_non_alphabetic_characters():
    assert decode_shift("fgh123!@#") == "abc123!@#"