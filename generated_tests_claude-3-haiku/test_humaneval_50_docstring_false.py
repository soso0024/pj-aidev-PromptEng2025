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

def test_encode_shift_lowercase():
    assert encode_shift("hello") == "mjqqt"

def test_encode_shift_uppercase():
    assert encode_shift("WORLD") == "BTWQI"

def test_encode_shift_mixed_case():
    assert encode_shift("Hello World") == "Mjqqt Btwqi"

def test_encode_shift_non_alphabetic_chars():
    assert encode_shift("Hello, World!") == "Mjqqt, Btwqi!"

def test_decode_shift_empty_string():
    assert decode_shift("") == ""

def test_decode_shift_lowercase():
    assert decode_shift("mjqqt") == "hello"

def test_decode_shift_uppercase():
    assert decode_shift("BTWQI") == "WORLD"

def test_decode_shift_mixed_case():
    assert decode_shift("Mjqqt Btwqi") == "Hello World"

def test_decode_shift_non_alphabetic_chars():
    assert decode_shift("Mjqqt, Btwqi!") == "Hello, World!"