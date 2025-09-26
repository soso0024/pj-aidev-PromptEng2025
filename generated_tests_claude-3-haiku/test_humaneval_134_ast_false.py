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
from your_module import check_if_last_char_is_a_letter

@pytest.mark.parametrize("input_text, expected", [
    ("hello world", True),
    ("hello world!", False),
    ("", False),
    ("a", True),
    ("1", False),
    ("hello 123", True),
    ("hello world 123", True),
    ("hello world 1", False),
    ("hello world a", True),
    ("hello world A", False)
])
def test_check_if_last_char_is_a_letter(input_text, expected):
    assert check_if_last_char_is_a_letter(input_text) == expected

def test_check_if_last_char_is_a_letter_raises_error():
    with pytest.raises(TypeError):
        check_if_last_char_is_a_letter(123)