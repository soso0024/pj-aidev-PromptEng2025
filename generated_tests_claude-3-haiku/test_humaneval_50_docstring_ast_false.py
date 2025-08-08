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
from .encode_shift import encode_shift
from .decode_shift import decode_shift

def test_encode_shift_empty_string():
    assert encode_shift('') == ''

def test_encode_shift_single_character():
    assert encode_shift('a') == 'f'
    assert encode_shift('z') == 'e'

def test_encode_shift_mixed_case():
    assert encode_shift('Hello World') == 'Mjqqt Btwqi'

def test_encode_shift_non_alphabetic_characters():
    assert encode_shift('Hello123 World!') == 'Mjqqt123 Btwqi!'

def test_decode_shift_empty_string():
    assert decode_shift('') == ''

def test_decode_shift_single_character():
    assert decode_shift('f') == 'a'
    assert decode_shift('e') == 'z'

def test_decode_shift_mixed_case():
    assert decode_shift('Mjqqt Btwqi') == 'Hello World'

def test_decode_shift_non_alphabetic_characters():
    assert decode_shift('Mjqqt123 Btwqi!') == 'Hello123 World!'