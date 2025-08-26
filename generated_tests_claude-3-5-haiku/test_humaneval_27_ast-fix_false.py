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
    if string is None:
        raise TypeError("Input cannot be None")
    return string.swapcase()

def test_flip_case_basic_lowercase():
    assert flip_case("hello") == "HELLO"

def test_flip_case_basic_uppercase():
    assert flip_case("WORLD") == "world"

def test_flip_case_mixed_case():
    assert flip_case("HeLLo") == "hEllO"

def test_flip_case_empty_string():
    assert flip_case("") == ""

def test_flip_case_with_numbers():
    assert flip_case("Hello123") == "hELLO123"

def test_flip_case_with_special_characters():
    assert flip_case("Hello, World!") == "hELLO, wORLD!"

def test_flip_case_unicode_characters():
    assert flip_case("Héllö") == "hÉLLÖ"

@pytest.mark.parametrize("input_str,expected", [
    ("hello", "HELLO"),
    ("WORLD", "world"),
    ("MixEd", "mIxeD"),
    ("", ""),
    ("123", "123"),
    ("Hello, World!", "hELLO, wORLD!")
])
def test_flip_case_parametrized(input_str, expected):
    assert flip_case(input_str) == expected

def test_flip_case_none_input():
    with pytest.raises(TypeError):
        flip_case(None)