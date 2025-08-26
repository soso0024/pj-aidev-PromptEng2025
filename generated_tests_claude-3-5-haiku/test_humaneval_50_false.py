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

def test_decode_shift_basic():
    assert decode_shift('fqjcbusdwvxzgwfyqtpmc') == 'alphabeticalorder'

def test_decode_shift_empty_string():
    assert decode_shift('') == ''

def test_decode_shift_single_character():
    assert decode_shift('k') == 'f'

def test_decode_shift_multiple_characters():
    assert decode_shift('fqjcbusdwvxzgwfyqtpnb') == 'alphabeticalorde'

@pytest.mark.parametrize("input_str,expected", [
    ('fqjcbusdwvxzgwfyqtpmc', 'alphabeticalorder'),
    ('', ''),
    ('k', 'f'),
    ('fqjcbusdwvxzgwfyqtpnb', 'alphabeticalorde')
])
def test_decode_shift_parametrized(input_str, expected):
    assert decode_shift(input_str) == expected

def test_decode_shift_wrapping():
    assert decode_shift('a') == 'v'
    assert decode_shift('v') == 'q'