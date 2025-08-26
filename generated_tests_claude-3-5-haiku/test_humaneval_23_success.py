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

def test_strlen_normal_cases():
    assert strlen("hello") == 5
    assert strlen("") == 0
    assert strlen("123") == 3

def test_strlen_unicode_strings():
    assert strlen("こんにちは") == 5
    assert strlen("🌍🌎🌏") == 3

def test_strlen_whitespace_strings():
    assert strlen(" ") == 1
    assert strlen("   ") == 3
    assert strlen("\t\n") == 2

@pytest.mark.parametrize("input_string,expected_length", [
    ("", 0),
    ("a", 1),
    ("hello world", 11),
    ("123!@#", 6),
    ("   trim   ", 10)
])
def test_strlen_parametrized(input_string, expected_length):
    assert strlen(input_string) == expected_length

def test_strlen_type_error():
    with pytest.raises(TypeError):
        strlen(123)
    with pytest.raises(TypeError):
        strlen(None)
