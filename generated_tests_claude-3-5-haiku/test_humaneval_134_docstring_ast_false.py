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
    txt = txt.rstrip()
    if not txt:
        return False
    check = txt.split()[-1]
    return len(check) == 1 and check.isalpha()

def test_check_if_last_char_is_a_letter():
    assert check_if_last_char_is_a_letter("apple pi e") == True
    assert check_if_last_char_is_a_letter("apple pie") == False
    assert check_if_last_char_is_a_letter("apple pi e ") == False
    assert check_if_last_char_is_a_letter("") == False

@pytest.mark.parametrize("input_str,expected", [
    ("hello world a", True),
    ("hello world", False),
    ("a b c", True),
    ("a b c ", False),
    ("single", False),
    ("multiple words ending with x", False),
    ("multiple words ending with x ", False),
    ("test case with space e", True),
    ("   trailing space z", True),
    ("z", True)
])
def test_check_if_last_char_is_a_letter_parametrized(input_str, expected):
    assert check_if_last_char_is_a_letter(input_str) == expected

def test_check_if_last_char_is_a_letter_edge_cases():
    assert check_if_last_char_is_a_letter(" a") == True
    assert check_if_last_char_is_a_letter("a ") == False
    assert check_if_last_char_is_a_letter("  a  ") == True