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

def test_encrypt_lowercase_string():
    assert encrypt('hello') == 'lipps'

def test_encrypt_uppercase_string():
    assert encrypt('WORLD') == 'XPSME'

def test_encrypt_mixed_case_string():
    assert encrypt('Hello World') == 'Lipps Xpsme'

def test_encrypt_string_with_numbers():
    assert encrypt('Hello123World') == 'Lipps123Xpsme'

def test_encrypt_string_with_special_characters():
    assert encrypt('Hello@World!') == 'Lipps@Xpsme!'

@pytest.mark.parametrize("input,expected", [
    ('', ''),
    ('hello', 'lipps'),
    ('WORLD', 'XPSME'),
    ('Hello World', 'Lipps Xpsme'),
    ('Hello123World', 'Lipps123Xpsme'),
    ('Hello@World!', 'Lipps@Xpsme!')
])
def test_encrypt_with_parameterized_cases(input, expected):
    assert encrypt(input) == expected

def test_encrypt_none_input():
    with pytest.raises(TypeError):
        encrypt(None)