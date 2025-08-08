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
    assert flip_case("") == ""

def test_flip_case_single_lowercase():
    assert flip_case("a") == "A"

def test_flip_case_single_uppercase():
    assert flip_case("Z") == "z"

def test_flip_case_mixed_case():
    assert flip_case("Hello World") == "hELLO wORLD"

def test_flip_case_all_uppercase():
    assert flip_case("PYTHON") == "python"

def test_flip_case_all_lowercase():
    assert flip_case("python") == "PYTHON"

@pytest.mark.parametrize("input_str,expected", [
    ("Hello, World!", "hELLO, wORLD!"),
    ("Python3.9", "pYTHON3.9"),
    ("12345", "12345"),
    ("!@#$%", "!@#$%"),
    ("aA bB cC", "Aa Bb Cc"),
    ("   ", "   "),
    ("Mixed_Case_String", "mIXED_cASE_sTRING"),
    ("PyTest-Example", "pYtEST-eXAMPLE")
])
def test_flip_case_parametrized(input_str, expected):
    assert flip_case(input_str) == expected

def test_flip_case_special_chars():
    assert flip_case("Hello\nWorld") == "hELLO\nwORLD"

def test_flip_case_unicode():
    assert flip_case("Café") == "cAFÉ"

def test_flip_case_type_error():
    with pytest.raises(AttributeError):
        flip_case(None)

def test_flip_case_non_string():
    with pytest.raises(AttributeError):
        flip_case(123)
