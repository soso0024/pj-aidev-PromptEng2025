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

def test_check_if_last_char_is_a_letter_single_letter_word():
    assert check_if_last_char_is_a_letter("hello a") == True

def test_check_if_last_char_is_a_letter_multiple_words():
    assert check_if_last_char_is_a_letter("this is a test b") == True

def test_check_if_last_char_is_a_letter_non_letter_end():
    assert check_if_last_char_is_a_letter("test 123") == False

def test_check_if_last_char_is_a_letter_empty_string():
    assert check_if_last_char_is_a_letter("") == False

def test_check_if_last_char_is_a_letter_uppercase():
    assert check_if_last_char_is_a_letter("HELLO Z") == True

@pytest.mark.parametrize("input_text,expected", [
    ("hello a", True),
    ("test b", True),
    ("python 3 x", True),
    ("coding z", True),
    ("test 123", False),
    ("number 42", False),
    ("", False),
    ("single", False),
    ("multiple words 9", False)
])
def test_check_if_last_char_is_a_letter_parametrized(input_text, expected):
    assert check_if_last_char_is_a_letter(input_text) == expected

def test_check_if_last_char_is_a_letter_special_characters():
    assert check_if_last_char_is_a_letter("test! x") == True

def test_check_if_last_char_is_a_letter_whitespace_only():
    assert check_if_last_char_is_a_letter(" ") == False
