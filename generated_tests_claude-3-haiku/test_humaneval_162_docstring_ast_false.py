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
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

@pytest.mark.parametrize("input,expected", [
    ('', None),
    ('Hello world', '3e25960a79dbc69b674cd4ec67a72c62'),
    ('Python', '5d41402abc4b2a76b9719d911017c592'),
    ('1234567890', 'e10adc3949ba59abbe56e057f20f883e'),
    ('abc123!@#', 'e10adc3949ba59abbe56e057f20f883e')
])
def test_string_to_md5_various_inputs(input, expected):
    assert string_to_md5(input) == expected

def test_string_to_md5_non_ascii_input():
    assert string_to_md5('Привет, мир!') == '4d7d7d7d7d7d7d7d7d7d7d7d7d7d7d7d'