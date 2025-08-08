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
    if not s:
        return s
    
    if not all(ch.islower() for ch in s):
        raise ValueError("Input must be lowercase alphabetic characters")
    
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

def test_decode_shift_normal_cases():
    assert decode_shift('fqjcbusdwvxzgwzqxfuqalrntsvruzgxsxkqfqunzglk') == 'abcdefghijklmnopqrstuvwxyz'
    assert decode_shift('bqebihjnqr') == 'welcome'
    assert decode_shift('') == ''

def test_decode_shift_single_character():
    assert decode_shift('f') == 'a'
    assert decode_shift('z') == 'u'

@pytest.mark.parametrize("input_str,expected", [
    ('fqjcbusdwvxzgwzqxfuqalrntsvruzgxsxkqfqunzglk', 'abcdefghijklmnopqrstuvwxyz'),
    ('bqebihjnqr', 'welcome'),
    ('', ''),
    ('f', 'a'),
    ('z', 'u')
])
def test_decode_shift_parametrized(input_str, expected):
    assert decode_shift(input_str) == expected

def test_decode_shift_case_sensitivity():
    with pytest.raises(ValueError):
        decode_shift('UPPERCASE')
    with pytest.raises(ValueError):
        decode_shift('MixedCase')

def test_decode_shift_non_alphabetic():
    with pytest.raises(ValueError):
        decode_shift('123')
    with pytest.raises(ValueError):
        decode_shift('!@#')