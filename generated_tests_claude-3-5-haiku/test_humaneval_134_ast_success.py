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

def test_check_if_last_char_is_a_letter():
    assert check_if_last_char_is_a_letter("hello world a") == True
    assert check_if_last_char_is_a_letter("hello world b") == True
    assert check_if_last_char_is_a_letter("hello world 1") == False
    assert check_if_last_char_is_a_letter("hello world !") == False

@pytest.mark.parametrize("input_text,expected", [
    ("hello world a", True),
    ("hello world z", True),
    ("hello world A", True),
    ("hello world Z", True),
    ("hello world 1", False),
    ("hello world !", False),
    ("single a", True),
    ("single Z", True),
    ("", False),
    ("multiple words with a", True),
    ("multiple words with Z", True)
])
def test_check_if_last_char_is_a_letter_parametrized(input_text, expected):
    assert check_if_last_char_is_a_letter(input_text) == expected

def test_check_if_last_char_is_a_letter_edge_cases():
    assert check_if_last_char_is_a_letter("a") == True
    assert check_if_last_char_is_a_letter("Z") == True
    assert check_if_last_char_is_a_letter(" a") == True
    assert check_if_last_char_is_a_letter(" Z") == True

def test_check_if_last_char_is_a_letter_negative_cases():
    assert check_if_last_char_is_a_letter("hello world 1") == False
    assert check_if_last_char_is_a_letter("hello world !") == False
    assert check_if_last_char_is_a_letter("123") == False
    assert check_if_last_char_is_a_letter("") == False
