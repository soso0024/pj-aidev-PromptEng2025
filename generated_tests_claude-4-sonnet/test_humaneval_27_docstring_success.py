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

def flip_case(string: str) -> str:
    return string.swapcase()

def test_flip_case_basic():
    assert flip_case('Hello') == 'hELLO'

def test_flip_case_empty_string():
    assert flip_case('') == ''

def test_flip_case_all_lowercase():
    assert flip_case('hello') == 'HELLO'

def test_flip_case_all_uppercase():
    assert flip_case('HELLO') == 'hello'

def test_flip_case_mixed_case():
    assert flip_case('HeLLo WoRLd') == 'hEllO wOrlD'

def test_flip_case_numbers():
    assert flip_case('Hello123') == 'hELLO123'

def test_flip_case_special_characters():
    assert flip_case('Hello!@#$%') == 'hELLO!@#$%'

def test_flip_case_spaces():
    assert flip_case('Hello World') == 'hELLO wORLD'

def test_flip_case_single_character_lower():
    assert flip_case('a') == 'A'

def test_flip_case_single_character_upper():
    assert flip_case('A') == 'a'

def test_flip_case_single_character_number():
    assert flip_case('1') == '1'

def test_flip_case_single_character_special():
    assert flip_case('!') == '!'

@pytest.mark.parametrize("input_str,expected", [
    ("abc", "ABC"),
    ("ABC", "abc"),
    ("AbC", "aBc"),
    ("123", "123"),
    ("!@#", "!@#"),
    ("Hello World!", "hELLO wORLD!"),
    ("PyThOn", "pYtHoN"),
    ("   ", "   "),
    ("a1B2c3", "A1b2C3"),
    ("MiXeD cAsE 123!", "mIxEd CaSe 123!")
])
def test_flip_case_parametrized(input_str, expected):
    assert flip_case(input_str) == expected

def test_flip_case_unicode_letters():
    assert flip_case('Café') == 'cAFÉ'

def test_flip_case_newlines_and_tabs():
    assert flip_case('Hello\nWorld\t!') == 'hELLO\nwORLD\t!'

def test_flip_case_long_string():
    long_input = 'A' * 1000 + 'b' * 1000
    expected = 'a' * 1000 + 'B' * 1000
    assert flip_case(long_input) == expected