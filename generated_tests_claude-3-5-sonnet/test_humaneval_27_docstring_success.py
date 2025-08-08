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
    assert flip_case("Hello") == "hELLO"
    assert flip_case("WORLD") == "world"
    assert flip_case("python") == "PYTHON"

@pytest.mark.parametrize("input_str,expected", [
    ("Hello, World!", "hELLO, wORLD!"),
    ("", ""),
    ("123", "123"),
    ("PyThOn", "pYtHoN"),
    ("   ", "   "),
    ("!@#$%", "!@#$%"),
    ("aA bB cC", "Aa Bb Cc"),
    ("UPPER lower", "upper LOWER"),
    ("Mixed_Case_123", "mIXED_cASE_123"),
    ("Hello\nWorld", "hELLO\nwORLD"),
])
def test_flip_case_parametrized(input_str, expected):
    assert flip_case(input_str) == expected

def test_flip_case_special_chars():
    assert flip_case("áéíóú") == "ÁÉÍÓÚ"
    assert flip_case("ÁÉÍÓÚ") == "áéíóú"
    assert flip_case("ñÑ") == "Ññ"

def test_flip_case_with_spaces():
    assert flip_case("   Hello   ") == "   hELLO   "
    assert flip_case("\t\nTest\t\n") == "\t\ntEST\t\n"

def test_flip_case_type_error():
    with pytest.raises(AttributeError):
        flip_case(None)
    
    with pytest.raises(AttributeError):
        flip_case(123)

def test_flip_case_unicode():
    assert flip_case("Hello™®") == "hELLO™®"
    assert flip_case("über") == "ÜBER"