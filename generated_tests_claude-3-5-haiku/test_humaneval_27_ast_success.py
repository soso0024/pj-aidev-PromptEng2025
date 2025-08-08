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

def test_flip_case_lowercase():
    assert flip_case("hello") == "HELLO"

def test_flip_case_uppercase():
    assert flip_case("WORLD") == "world"

def test_flip_case_mixed_case():
    assert flip_case("HeLLo") == "hEllO"

def test_flip_case_with_numbers():
    assert flip_case("Hello123") == "hELLO123"

def test_flip_case_with_special_chars():
    assert flip_case("Hello, World!") == "hELLO, wORLD!"

def test_flip_case_empty_string():
    assert flip_case("") == ""

def test_flip_case_whitespace():
    assert flip_case("  Spaces  ") == "  sPACES  "

@pytest.mark.parametrize("input_str,expected", [
    ("hello", "HELLO"),
    ("WORLD", "world"),
    ("HeLLo", "hEllO"),
    ("Hello123", "hELLO123"),
    ("Hello, World!", "hELLO, wORLD!"),
    ("", ""),
    ("  Spaces  ", "  sPACES  ")
])
def test_flip_case_parametrized(input_str, expected):
    assert flip_case(input_str) == expected

def test_flip_case_unicode():
    assert flip_case("Héllö") == "hÉLLÖ"
