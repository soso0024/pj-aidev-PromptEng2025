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

def test_string_to_md5_normal_case():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

@pytest.mark.parametrize("input,expected", [
    ("test", "098f6bcd4621d373cade4e832627b4f6"),
    ("another", "900150983cd24fb0d6963f7d28e17f72"),
    ("python", "e10adc3949ba59abbe56e057f20f883e"),
    ("1234567890", "e10adc3949ba59abbe56e057f20f883e"),
    ("!@#$%^&*()_+", "7c6a180b36896a0a8c02787eeafb0e4c")
])
def test_string_to_md5_various_inputs(input, expected):
    assert string_to_md5(input) == expected

def test_string_to_md5_non_ascii_input():
    with pytest.raises(UnicodeEncodeError):
        string_to_md5('Héllö wörld')