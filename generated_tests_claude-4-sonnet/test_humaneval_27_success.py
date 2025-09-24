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

def flip_case(string: str):
    return string.swapcase()

def test_flip_case_empty_string():
    assert flip_case("") == ""

def test_flip_case_single_lowercase():
    assert flip_case("a") == "A"

def test_flip_case_single_uppercase():
    assert flip_case("A") == "a"

def test_flip_case_mixed_case():
    assert flip_case("Hello") == "hELLO"

def test_flip_case_all_lowercase():
    assert flip_case("hello") == "HELLO"

def test_flip_case_all_uppercase():
    assert flip_case("HELLO") == "hello"

def test_flip_case_with_numbers():
    assert flip_case("Hello123") == "hELLO123"

def test_flip_case_with_special_characters():
    assert flip_case("Hello!@#") == "hELLO!@#"

def test_flip_case_with_spaces():
    assert flip_case("Hello World") == "hELLO wORLD"

def test_flip_case_only_numbers():
    assert flip_case("12345") == "12345"

def test_flip_case_only_special_characters():
    assert flip_case("!@#$%") == "!@#$%"

def test_flip_case_only_spaces():
    assert flip_case("   ") == "   "

@pytest.mark.parametrize("input_str,expected", [
    ("abc", "ABC"),
    ("ABC", "abc"),
    ("AbC", "aBc"),
    ("123abc", "123ABC"),
    ("abc123", "ABC123"),
    ("a1B2c3", "A1b2C3"),
    ("Hello, World!", "hELLO, wORLD!"),
    ("PyThOn", "pYtHoN"),
    ("TEST_case", "test_CASE"),
    ("MiXeD123!@#", "mIxEd123!@#")
])
def test_flip_case_parametrized(input_str, expected):
    assert flip_case(input_str) == expected

def test_flip_case_unicode_characters():
    assert flip_case("Héllo") == "hÉLLO"

def test_flip_case_newlines_and_tabs():
    assert flip_case("Hello\nWorld\t") == "hELLO\nwORLD\t"

def test_flip_case_long_string():
    long_str = "A" * 1000 + "b" * 1000
    expected = "a" * 1000 + "B" * 1000
    assert flip_case(long_str) == expected

def test_flip_case_type_error():
    with pytest.raises(AttributeError):
        flip_case(None)

def test_flip_case_type_error_int():
    with pytest.raises(AttributeError):
        flip_case(123)

def test_flip_case_type_error_list():
    with pytest.raises(AttributeError):
        flip_case([])
