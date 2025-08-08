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

def test_encrypt_basic_cases():
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'

def test_encrypt_empty_string():
    assert encrypt('') == ''

def test_encrypt_mixed_case():
    assert encrypt('HI') == 'lm'
    assert encrypt('Hello') == 'lipps'

def test_encrypt_non_alphabetic():
    assert encrypt('123!@#') == '123!@#'
    assert encrypt('hello world') == 'lipps asvph'

def test_encrypt_full_alphabet():
    assert encrypt('abcdefghijklmnopqrstuvwxyz') == 'efghijklmnopqrstuvwxyzab'

def test_encrypt_edge_cases():
    assert encrypt('zz') == 'dd'
    assert encrypt('xy') == 'ab'

@pytest.mark.parametrize("input_str,expected", [
    ('hi', 'lm'),
    ('asdfghjkl', 'ewhjklnop'),
    ('gf', 'kj'),
    ('et', 'ix'),
    ('', ''),
    ('123!@#', '123!@#'),
    ('hello world', 'lipps asvph'),
    ('zz', 'dd'),
    ('xy', 'ab')
])
def test_encrypt_parametrized(input_str, expected):
    assert encrypt(input_str) == expected