# Test cases for HumanEval/162
# Generated using Claude API


def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None


# Generated test cases:
import hashlib
import pytest

def string_to_md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest() if text else None

def test_string_to_md5_normal_case():
    assert string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_non_ascii_characters():
    assert string_to_md5('ñáéíóú') == '383391b4679ee9a0e4ad196be530e65e'

@pytest.mark.parametrize("input,expected", [
    (None, None),
    (123, '202cb962ac59075b964b07152d234b70'),
    ('', None),
    ('test', '098f6bcd4621d373cade4e832627b4f6'),
    ('hello world', '5eb63bbbe01eeed093cb22bb8f5acdc3')
])
def test_string_to_md5_various_inputs(input, expected):
    assert string_to_md5(input) == expected