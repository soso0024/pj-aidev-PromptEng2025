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

def test_empty_string():
    assert check_if_last_char_is_a_letter("") == False

@pytest.mark.parametrize("input_str, expected", [
    ("apple pie", False),
    ("apple pi e", True),
    ("apple pi e ", False),
    ("hello a", True),
    ("test x", True),
    ("test 1", False),
    ("test !", False),
    ("single", False),
    ("multiple words here", False),
    ("multiple words e", True),
    ("A B C D E", True),
    ("test. a", True),
    ("test.a", False),
    ("  ", False),
    ("a", True),  # Changed to True since single letter is a valid case
    ("a ", False),
    ("? e", True),
    ("123 z", True),
    ("ABC Z", True),
    ("test\n", False),
    ("test\t", False),
    ("test y ", False),
])
def test_last_char_is_letter(input_str, expected):
    assert check_if_last_char_is_a_letter(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "test A",
    "test a",
    "test Z",
    "test z",
])
def test_different_case_letters(input_str):
    assert check_if_last_char_is_a_letter(input_str) == True

@pytest.mark.parametrize("input_str", [
    "test 1",
    "test @",
    "test #",
    "test $",
    "test %",
    "test &",
    "test *",
])
def test_non_letter_characters(input_str):
    assert check_if_last_char_is_a_letter(input_str) == False

def test_unicode_characters():
    assert check_if_last_char_is_a_letter("test é") == False
    assert check_if_last_char_is_a_letter("test ñ") == False
    assert check_if_last_char_is_a_letter("test 汉") == False