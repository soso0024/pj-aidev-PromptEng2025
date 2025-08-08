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
    assert check_if_last_char_is_a_letter("apple pie") == False
    assert check_if_last_char_is_a_letter("apple pi e") == True
    assert check_if_last_char_is_a_letter("apple pi e ") == False
    assert check_if_last_char_is_a_letter("") == False

@pytest.mark.parametrize("input_str,expected", [
    ("hello world", False),
    ("hello world a", True),
    ("hello world a ", False),
    ("a", True),
    ("", False),
    ("multiple words here x", True),
    ("multiple words here x ", False),
    ("123 abc", False),
    ("123 a", True)
])
def test_check_if_last_char_is_a_letter_parametrized(input_str, expected):
    assert check_if_last_char_is_a_letter(input_str) == expected

def test_check_if_last_char_is_a_letter_edge_cases():
    assert check_if_last_char_is_a_letter(" x") == True
    assert check_if_last_char_is_a_letter("word x ") == False
    assert check_if_last_char_is_a_letter("x ") == False
