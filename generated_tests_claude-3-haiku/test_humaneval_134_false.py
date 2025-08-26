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

def test_check_if_last_char_is_a_letter_normal_case():
    assert check_if_last_char_is_a_letter("hello world") == True
    assert check_if_last_char_is_a_letter("python 3") == True
    assert check_if_last_char_is_a_letter("coding is fun") == True

def test_check_if_last_char_is_a_letter_edge_cases():
    assert check_if_last_char_is_a_letter("") == False
    assert check_if_last_char_is_a_letter(" ") == False
    assert check_if_last_char_is_a_letter("123") == False
    assert check_if_last_char_is_a_letter("hello world ") == True

@pytest.mark.parametrize("input,expected", [
    ("hello", True),
    ("world 123", False),
    ("python3", True),
    ("coding is fun!", True),
    ("a", True),
    ("1", False),
    (" ", False),
    ("", False)
])
def test_check_if_last_char_is_a_letter_parametrized(input, expected):
    assert check_if_last_char_is_a_letter(input) == expected

def check_if_last_char_is_a_letter(txt):
    if not txt.strip():
        return False
    check = txt.split()[-1]
    return len(check) == 1 and (97 <= ord(check.lower()) <= 122)