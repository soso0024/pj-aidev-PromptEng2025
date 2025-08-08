# Test cases for HumanEval/89
# Generated using Claude API


def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """

    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out


# Generated test cases:
import pytest

def test_encrypt_empty_string():
    assert encrypt('') == ''

@pytest.mark.parametrize("input,expected", [
    ('hi', 'lm'),
    ('asdfghjkl', 'ewhjklnop'),
    ('gf', 'kj'),
    ('et', 'ix'),
    ('abc', 'efj'),
    ('xyz', 'bcd')
])
def test_encrypt_normal_cases(input, expected):
    assert encrypt(input) == expected

def test_encrypt_non_alphabetic_characters():
    assert encrypt('123!@#') == '123!@#'

def test_encrypt_mixed_case():
    assert encrypt('HeLlO') == 'KeNnQ'

def test_encrypt_long_string():
    long_string = 'The quick brown fox jumps over the lazy dog.'
    expected = 'Vjg swkem dtqyp hqz lworru qxgt vjg ncba fqi.'
    assert encrypt(long_string) == expected