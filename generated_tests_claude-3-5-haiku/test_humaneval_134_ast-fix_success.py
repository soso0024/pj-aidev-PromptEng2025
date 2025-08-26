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

def test_last_char_is_letter_single_letter():
    assert check_if_last_char_is_a_letter('hello a') == True
    assert check_if_last_char_is_a_letter('test z') == True

def test_last_char_is_letter_multiple_words():
    assert check_if_last_char_is_a_letter('hello world x') == True
    assert check_if_last_char_is_a_letter('multiple words y') == True

def test_last_char_is_not_letter():
    assert check_if_last_char_is_a_letter('hello 1') == False
    assert check_if_last_char_is_a_letter('test !') == False
    assert check_if_last_char_is_a_letter('multiple words 5') == False

def test_last_char_is_letter_case_insensitive():
    assert check_if_last_char_is_a_letter('hello A') == True
    assert check_if_last_char_is_a_letter('test Z') == True

def test_empty_string():
    assert check_if_last_char_is_a_letter('') == False

@pytest.mark.parametrize("input_text,expected", [
    ('hello a', True),
    ('test z', True),
    ('hello world x', True),
    ('hello 1', False),
    ('test !', False),
    ('', False),
    ('hello A', True),
    ('multiple words 5', False)
])
def test_check_if_last_char_is_a_letter_parametrized(input_text, expected):
    assert check_if_last_char_is_a_letter(input_text) == expected
