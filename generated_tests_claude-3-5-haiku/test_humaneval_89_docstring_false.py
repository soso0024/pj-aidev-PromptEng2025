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

def test_encrypt_basic_lowercase():
    assert encrypt('hi') == 'lm'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'

def test_encrypt_full_alphabet():
    assert encrypt('asdfghjkl') == 'ewhjklnop'

def test_encrypt_mixed_case():
    assert encrypt('HI') == 'HI'
    assert encrypt('Hello') == 'Hello'

def test_encrypt_empty_string():
    assert encrypt('') == ''

def test_encrypt_special_characters():
    assert encrypt('hello!') == 'lipps!'
    assert encrypt('123abc') == '123ewh'

def test_encrypt_wrap_around():
    assert encrypt('yz') == 'cd'

@pytest.mark.parametrize("input_str,expected", [
    ('hi', 'lm'),
    ('gf', 'kj'),
    ('et', 'ix'),
    ('asdfghjkl', 'ewhjklnop'),
    ('', ''),
    ('hello!', 'lipps!'),
    ('yz', 'cd')
])
def test_encrypt_parametrized(input_str, expected):
    assert encrypt(input_str) == expected