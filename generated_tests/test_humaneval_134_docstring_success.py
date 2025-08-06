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

@pytest.mark.parametrize("input_str, expected", [
    ("apple pie", False),
    ("apple pi e", True),
    ("apple pi e ", False),
    ("", False),
    ("hello a", True),
    ("test z", True),
    ("multiple words x", True),
    ("ends with space ", False),
    ("single", False),
    ("123 a", True),
    ("!@# x", True),
    ("mixed 123 A", True),
    ("a", True),
    ("A", True),
    ("1", False),
    ("hello Z", True),
    ("test 9", False),
    ("test !", False),
    ("multiple   spaces    a", True),
    ("tab\ta", False)
])
def test_check_if_last_char_is_a_letter(input_str, expected):
    assert check_if_last_char_is_a_letter(input_str) == expected

def test_check_if_last_char_is_a_letter_with_none():
    with pytest.raises(AttributeError):
        check_if_last_char_is_a_letter(None)

def test_check_if_last_char_is_a_letter_with_non_string():
    with pytest.raises(AttributeError):
        check_if_last_char_is_a_letter(123)

def test_check_if_last_char_is_a_letter_with_special_chars():
    assert check_if_last_char_is_a_letter("test #") == False
    assert check_if_last_char_is_a_letter("test $") == False
    assert check_if_last_char_is_a_letter("test @") == False

def test_check_if_last_char_is_a_letter_with_numbers():
    assert check_if_last_char_is_a_letter("test 1") == False
    assert check_if_last_char_is_a_letter("test 42") == False
    assert check_if_last_char_is_a_letter("numbers 0") == False