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

def check_if_last_char_is_a_letter(txt):
    check = txt.strip().split()
    if not check:
        return False
    last_char = check[-1]
    return len(last_char) == 1 and last_char.isalpha()

def test_check_if_last_char_is_a_letter():
    assert check_if_last_char_is_a_letter("hello world") == False
    assert check_if_last_char_is_a_letter("hello world ") == False
    assert check_if_last_char_is_a_letter("hello world123") == False
    assert check_if_last_char_is_a_letter("") == False
    assert check_if_last_char_is_a_letter("a") == True
    assert check_if_last_char_is_a_letter("A") == True
    assert check_if_last_char_is_a_letter("1 a") == True
    assert check_if_last_char_is_a_letter("1 A") == True

@pytest.mark.parametrize("input,expected", [
    ("hello world", False),
    ("hello world ", False),
    ("hello world123", False),
    ("", False),
    ("a", True),
    ("A", True),
    ("1 a", True),
    ("1 A", True)
])
def test_check_if_last_char_is_a_letter_parametrized(input, expected):
    assert check_if_last_char_is_a_letter(input) == expected