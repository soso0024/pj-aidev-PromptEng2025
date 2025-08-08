# Test cases for HumanEval/27
# Generated using Claude API



def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    return string.swapcase()


# Generated test cases:
import pytest

def test_flip_case_empty_string():
    assert flip_case('') == ''

def test_flip_case_all_lowercase():
    assert flip_case('hello') == 'HELLO'

def test_flip_case_all_uppercase():
    assert flip_case('WORLD') == 'world'

def test_flip_case_mixed_case():
    assert flip_case('Hello World') == 'hELLO wORLD'

@pytest.mark.parametrize("input,expected", [
    ('123ABC', '123abc'),
    ('abc123', 'ABC123'),
    ('Aa Bb Cc', 'aA bB cC'),
    ('1A2b3C', '1a2B3c'),
    ('!@#$%^&*', '!@#$%^&*')
])
def test_flip_case_various_inputs(input, expected):
    assert flip_case(input) == expected

def test_flip_case_non_string_input():
    with pytest.raises(TypeError):
        flip_case(123)