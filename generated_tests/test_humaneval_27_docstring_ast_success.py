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

def test_basic_string():
    assert flip_case("Hello") == "hELLO"
    assert flip_case("WORLD") == "world"
    assert flip_case("python") == "PYTHON"

@pytest.mark.parametrize("input_str,expected", [
    ("", ""),
    ("a", "A"),
    ("Z", "z"),
    ("Hello World!", "hELLO wORLD!"),
    ("Python3.9", "pYTHON3.9"),
    ("123", "123"),
    ("!@#$", "!@#$"),
    ("Mixed CASE 123", "mIXED case 123"),
    ("  spaces  ", "  SPACES  "),
    ("CamelCase", "cAMELcASE"),
    ("snake_case", "SNAKE_CASE"),
    ("12345!@#$%", "12345!@#$%"),
    ("αβγδ", "ΑΒΓΔ"),  # Greek letters should be swapped
    ("Hello\nWorld", "hELLO\nwORLD"),
    ("Tab\tHere", "tAB\thERE")
])
def test_flip_case_parametrized(input_str, expected):
    assert flip_case(input_str) == expected

def test_empty_string():
    assert flip_case("") == ""

def test_single_character():
    assert flip_case("a") == "A"
    assert flip_case("Z") == "z"

def test_special_characters():
    assert flip_case("!@#$%^&*()") == "!@#$%^&*()"

def test_with_numbers():
    assert flip_case("123ABC123") == "123abc123"

def test_with_whitespace():
    assert flip_case("  Spaces  ") == "  sPACES  "
    assert flip_case("\t\nTest\t\n") == "\t\ntEST\t\n"

def test_type_error():
    with pytest.raises(AttributeError):
        flip_case(None)
    with pytest.raises(AttributeError):
        flip_case(123)

def test_unicode_strings():
    assert flip_case("Hello™®") == "hELLO™®"
    assert flip_case("étude") == "ÉTUDE"