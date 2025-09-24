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
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

@pytest.mark.parametrize("input_txt,expected", [
    ("a", True),
    ("z", True),
    ("A", True),
    ("Z", True),
    ("hello a", True),
    ("test Z", True),
    ("word b", True),
    ("", False),
    ("ab", False),
    ("hello", False),
    ("test word", False),
    ("hello 1", False),
    ("test 9", False),
    ("word @", False),
    ("text #", False),
    ("hello !", False),
    ("test $", False),
    ("word %", False),
    ("hello world", False),
    ("multiple words here", False),
    ("a b c d e", True),
    ("1 2 3 a", True),
    ("symbols @ # a", True),
    ("   a", True),
    ("hello   z", True),
    ("test  ", False),
    ("word   ", False),
    ("a ", False),
    ("hello a ", False),
    ("123", False),
    ("hello 123", False),
    ("test abc", False),
    ("word xyz", False),
    ("single", False),
    ("multiple", False),
    ("a1", False),
    ("1a", False),
    ("hello a1", False),
    ("test 1a", False),
    ("special chars !@#", False),
    ("numbers 123", False),
    ("mixed a1b", False),
    ("space test ", False),
    ("tab\ta", False),
    ("newline\na", False),
    ("multiple\tspaces\ta", False)
])
def test_check_if_last_char_is_a_letter(input_txt, expected):
    assert check_if_last_char_is_a_letter(input_txt) == expected

def test_empty_string():
    assert check_if_last_char_is_a_letter("") == False

def test_single_letter():
    assert check_if_last_char_is_a_letter("a") == True
    assert check_if_last_char_is_a_letter("Z") == True

def test_single_non_letter():
    assert check_if_last_char_is_a_letter("1") == False
    assert check_if_last_char_is_a_letter("@") == False

def test_multiple_words_ending_with_letter():
    assert check_if_last_char_is_a_letter("hello world a") == True
    assert check_if_last_char_is_a_letter("test case Z") == True

def test_multiple_words_ending_with_non_letter():
    assert check_if_last_char_is_a_letter("hello world 1") == False
    assert check_if_last_char_is_a_letter("test case @") == False

def test_multiple_words_ending_with_word():
    assert check_if_last_char_is_a_letter("hello world") == False
    assert check_if_last_char_is_a_letter("test case") == False

def test_trailing_spaces():
    assert check_if_last_char_is_a_letter("hello ") == False
    assert check_if_last_char_is_a_letter("test a ") == False

def test_multiple_spaces():
    assert check_if_last_char_is_a_letter("hello  a") == True
    assert check_if_last_char_is_a_letter("test   z") == True