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

def test_empty_string():
    assert flip_case("") == ""

def test_single_lowercase():
    assert flip_case("a") == "A"

def test_single_uppercase():
    assert flip_case("Z") == "z"

def test_mixed_case():
    assert flip_case("Hello World") == "hELLO wORLD"

@pytest.mark.parametrize("input_str,expected", [
    ("abc", "ABC"),
    ("ABC", "abc"),
    ("aBcDeF", "AbCdEf"),
    ("123", "123"),
    ("!@#", "!@#"),
    ("Hello, World!", "hELLO, wORLD!"),
    ("Python3.8", "pYTHON3.8"),
    ("   ", "   "),
    ("aA bB cC", "Aa Bb Cc"),
    ("UPPER lower", "upper LOWER"),
])
def test_various_strings(input_str, expected):
    assert flip_case(input_str) == expected

def test_special_characters():
    assert flip_case("Hello\nWorld") == "hELLO\nwORLD"
    assert flip_case("\t\n\r") == "\t\n\r"

def test_unicode_characters():
    assert flip_case("áéíóúÁÉÍÓÚ") == "ÁÉÍÓÚáéíóú"

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    ["string"],
    {"key": "value"},
    True,
    3.14
])
def test_invalid_input_type(invalid_input):
    with pytest.raises(AttributeError):
        flip_case(invalid_input)
