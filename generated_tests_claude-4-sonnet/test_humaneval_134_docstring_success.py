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
    ("apple pie", False),
    ("apple pi e", True),
    ("apple pi e ", False),
    ("", False),
    ("a", True),
    ("ab", False),
    ("hello world", False),
    ("hello w", True),
    ("test 1", False),
    ("test a", True),
    ("test A", True),
    ("test z", True),
    ("test Z", True),
    ("multiple spaces  ", False),
    ("multiple spaces  a", True),
    ("tab\t", False),
    ("newline\n", False),
    ("special!", False),
    ("special @", False),
    ("special #", False),
    ("number 5", False),
    ("number 0", False),
    ("single space ", False),
    ("double  space", False),
    ("double  s", True),
    ("triple   space", False),
    ("triple   s", True),
    ("x y z", True),
    ("x y zz", False),
    ("punctuation.", False),
    ("punctuation,", False),
    ("punctuation;", False),
    ("punctuation:", False),
    ("punctuation?", False),
    ("unicode é", False),
    ("unicode ñ", False),
    ("mixed Case", False),
    ("mixed C", True),
    ("   ", False),
    ("leading space", False),
    ("leading s", True),
    ("123", False),
    ("123 a", True),
    ("symbols @#$", False),
    ("symbols @#$ a", True)
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
    assert check_if_last_char_is_a_letter("!") == False
    assert check_if_last_char_is_a_letter(" ") == False

def test_word_ending():
    assert check_if_last_char_is_a_letter("word") == False
    assert check_if_last_char_is_a_letter("multiple words") == False

def test_single_letter_after_space():
    assert check_if_last_char_is_a_letter("word a") == True
    assert check_if_last_char_is_a_letter("multiple words x") == True

def test_trailing_spaces():
    assert check_if_last_char_is_a_letter("word ") == False
    assert check_if_last_char_is_a_letter("word a ") == False
    assert check_if_last_char_is_a_letter("word  ") == False

def test_multiple_spaces():
    assert check_if_last_char_is_a_letter("word  a") == True
    assert check_if_last_char_is_a_letter("word   b") == True
    assert check_if_last_char_is_a_letter("word    ") == False