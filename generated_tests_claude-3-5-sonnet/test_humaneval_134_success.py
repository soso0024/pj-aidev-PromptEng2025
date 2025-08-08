# Test cases for HumanEval/134
# Generated using Claude API


def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''

 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False


# Generated test cases:
import pytest

@pytest.mark.parametrize("input_str,expected", [
    ("Hello World a", True),
    ("Hello World Z", True),
    ("Hello World!", False),
    ("Hello World 1", False),
    ("Hello World  ", False),
    ("a", True),
    ("Z", True),
    ("", False),
    ("Hello World z", True),
    ("Test Case A", True),
    ("Multiple    Spaces    k", True),
    ("Symbols@#$%^&* x", True),
    ("Numbers123 4", False),
    ("Mixed123 A", True),
    ("Single!", False),
    ("  ", False),
    ("Hello World", False),
    ("Special Chars @", False),
    ("Tab x", True),
    ("Newline y", True)
])
def test_check_if_last_char_is_a_letter(input_str, expected):
    assert check_if_last_char_is_a_letter(input_str) == expected

def test_check_if_last_char_is_a_letter_with_none():
    with pytest.raises(AttributeError):
        check_if_last_char_is_a_letter(None)

def test_check_if_last_char_is_a_letter_with_number():
    with pytest.raises(AttributeError):
        check_if_last_char_is_a_letter(123)

def test_check_if_last_char_is_a_letter_with_boolean():
    with pytest.raises(AttributeError):
        check_if_last_char_is_a_letter(True)