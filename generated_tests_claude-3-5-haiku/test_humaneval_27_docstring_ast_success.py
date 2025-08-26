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

def test_flip_case_basic():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('world') == 'WORLD'
    assert flip_case('PytHON') == 'pYThon'

def test_flip_case_empty_string():
    assert flip_case('') == ''

def test_flip_case_mixed_case():
    assert flip_case('HeLLo WoRLd') == 'hEllO wOrlD'

def test_flip_case_special_characters():
    assert flip_case('Hello, World!') == 'hELLO, wORLD!'

def test_flip_case_numbers():
    assert flip_case('Hello123') == 'hELLO123'

@pytest.mark.parametrize("input_str,expected", [
    ('', ''),
    ('Hello', 'hELLO'),
    ('world', 'WORLD'),
    ('PytHON', 'pYThon'),
    ('Hello, World!', 'hELLO, wORLD!'),
    ('123ABC', '123abc')
])
def test_flip_case_parametrized(input_str, expected):
    assert flip_case(input_str) == expected