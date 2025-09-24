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
from encrypt import encrypt

@pytest.mark.parametrize("input_str, expected", [
    ('hi', 'lm'),
    ('asdfghjkl', 'ewhjklnop'),
    ('gf', 'kj'),
    ('et', 'ix'),
    ('', ''),
    ('123', '123'),
    ('HI', 'LM'),
    ('ASDFGHJKL', 'EWHJKLNOP'),
    ('GF', 'KJ'),
    ('ET', 'IX'),
    ('hello world', 'lipps asvph'),
    ('PYTHON', 'TZVJQP'),
    ('python', 'tzvjqp'),
    ('1a2b3c', '1e2f3g'),
    ('!@#$%^&*()_+', '!@#$%^&*()_+')
])
def test_encrypt(input_str, expected):
    assert encrypt(input_str) == expected