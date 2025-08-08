# Test cases for HumanEval/23
# Generated using Claude API



def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    return len(string)


# Generated test cases:
import pytest

def test_strlen_empty_string():
    assert strlen('') == 0

def test_strlen_normal_string():
    assert strlen('abc') == 3

def test_strlen_unicode_string():
    assert strlen('こんにちは') == 5

def test_strlen_whitespace_string():
    assert strlen('   ') == 3

def test_strlen_special_characters():
    assert strlen('!@#$%^&*()') == 10

@pytest.mark.parametrize("input_string,expected_length", [
    ('', 0),
    ('abc', 3),
    ('hello world', 11),
    ('123', 3),
    ('   ', 3),
    ('こんにちは', 5)
])
def test_strlen_parametrized(input_string, expected_length):
    assert strlen(input_string) == expected_length

def test_strlen_type_error():
    with pytest.raises(TypeError):
        strlen(123)

def test_strlen_none_error():
    with pytest.raises(TypeError):
        strlen(None)
