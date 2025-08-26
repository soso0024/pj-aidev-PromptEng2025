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

def test_last_char_is_letter_single_letter_word():
    assert check_if_last_char_is_a_letter('a') == True

def test_last_char_is_letter_multiple_word_sentence():
    assert check_if_last_char_is_a_letter('hello world x') == True

def test_last_char_is_letter_multiple_word_sentence_with_number():
    assert check_if_last_char_is_a_letter('hello world 123 x') == True

def test_last_char_is_not_letter_ends_with_number():
    assert check_if_last_char_is_a_letter('hello world 123') == False

def test_last_char_is_not_letter_ends_with_symbol():
    assert check_if_last_char_is_a_letter('hello world !') == False

def test_empty_string():
    assert check_if_last_char_is_a_letter('') == False

@pytest.mark.parametrize("input_text,expected", [
    ('test a', True),
    ('hello world x', True),
    ('multiple words ending with z', True),
    ('123 abc', True),
    ('hello 123', False),
    ('test!', False),
    ('', False),
    ('a b c', True)
])
def test_various_inputs(input_text, expected):
    assert check_if_last_char_is_a_letter(input_text) == expected

def test_case_insensitivity():
    assert check_if_last_char_is_a_letter('hello world A') == True
    assert check_if_last_char_is_a_letter('hello world Z') == True