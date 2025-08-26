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
import pytest
import hashlib

def test_string_to_md5_normal_case():
    assert string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_unicode_raises_error():
    with pytest.raises(UnicodeEncodeError):
        string_to_md5('こんにちは')

@pytest.mark.parametrize("input_text,expected", [
    ('hello', '5d41402abc4b2a76b9719d911017c592'),
    ('world', '7d793037a0760186e3b38bd7349a6f85'),
    ('', None),
    ('123', '202cb962ac59075b964b07152d234b70')
])
def test_string_to_md5_parametrized(input_text, expected):
    assert string_to_md5(input_text) == expected

def test_string_to_md5_none_input():
    assert string_to_md5(None) is None