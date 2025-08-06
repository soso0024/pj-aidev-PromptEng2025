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
    ("Hello a", True),
    ("Hello A", True),
    ("Hello z", True),
    ("Hello Z", True),
    ("Hello 1", False),
    ("Hello !", False),
    ("Hello  ", False),
    ("a", True),
    ("Z", True),
    ("Hello world h", True),
    ("Test case 5", False),
    ("Special char @", False),
    ("Multiple    spaces    k", True),
    ("Tab character a", True),
    ("Mixed123 cases K", True),
    ("", False),
    ("12345", False),
    ("!@#$%", False),
    ("Hello world.", False),
    ("Test with spaces   ", False)
])
def test_check_if_last_char_is_a_letter(input_str, expected):
    assert check_if_last_char_is_a_letter(input_str) == expected

def test_check_if_last_char_is_a_letter_empty_string():
    assert check_if_last_char_is_a_letter("") == False

def test_check_if_last_char_is_a_letter_single_letter():
    assert check_if_last_char_is_a_letter("a") == True

def test_check_if_last_char_is_a_letter_single_number():
    assert check_if_last_char_is_a_letter("5") == False

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    3.14,
    [],
    {},
    True
])
def test_check_if_last_char_is_a_letter_invalid_input(invalid_input):
    with pytest.raises(AttributeError):
        check_if_last_char_is_a_letter(invalid_input)