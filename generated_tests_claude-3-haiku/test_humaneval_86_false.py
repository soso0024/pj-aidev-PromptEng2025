# Test cases for HumanEval/86
# Generated using Claude API


def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """

    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


# Generated test cases:
from solution import anti_shuffle
import pytest

@pytest.mark.parametrize("input,expected", [
    ("hello world", "ehllo   dlrow"),
    ("python is awesome", "ahnoppty   is   emorssw"),
    ("", ""),
    ("   ", "   "),
    ("a b c", "a b c"),
    ("abc def ghi", "abc   def   ghi"),
    ("Hello World!", "Hel lo   Wdlor!"),
    ("1 2 3", "1 2 3"),
    ("a1 b2 c3", "a1   b2   c3"),
    ("a b c d e f g h i j", "a b c   d e f   g h i   j")
])
def test_anti_shuffle(input, expected):
    assert anti_shuffle(input) == expected

def test_anti_shuffle_raises_error():
    with pytest.raises(TypeError):
        anti_shuffle(123)