# Test cases for HumanEval/91
# Generated using Claude API


def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """

    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)


# Generated test cases:
import pytest

@pytest.mark.parametrize("input_str,expected", [
    ("Hello world", 0),
    ("The sky is blue. The sun is shining. I love this weather", 1),
    ("I am bored. I am very bored!", 2),
    ("", 0),
    ("I", 0),
    ("i am not counted. I am counted.", 1),
    ("Hello. World. Nice day.", 0),
    ("I love coding! I enjoy testing? I write tests.", 3),
    ("Not a boredom. i with lowercase.", 0),
    ("I.I.I", 0),
    ("I am. here.I am.there", 2),
    ("This is a test? I think so! I know it.", 2),
    ("   I am spaced.", 0),
    ("No boredom here", 0),
    ("I! I? I.", 0),
    ("Random text. More text! Even more text?", 0),
    ("I am first. You are second. They are third.", 1),
    ("Sentence one. I am sentence two! I am also sentence three?", 2)
])
def test_is_bored_parametrized(input_str, expected):
    result = is_bored(input_str)
    assert result == expected

def test_is_bored_empty():
    assert is_bored("") == 0

def test_is_bored_single_char():
    assert is_bored("I") == 0

def test_is_bored_multiple_spaces():
    assert is_bored("I    am spaced.    I   am also spaced.") == 2

def test_is_bored_no_spaces():
    assert is_bored("I.I.I") == 0

def test_is_bored_mixed_punctuation():
    assert is_bored("I am here! I am there? I am everywhere.") == 3

def test_is_bored_special_characters():
    assert is_bored("I'm here. I've been here. I'll be here.") == 0

def test_is_bored_case_sensitivity():
    assert is_bored("i am not counted. I am counted. IGNORE THIS.") == 1

def test_is_bored_with_leading_spaces():
    assert is_bored("   I am spaced.") == 0

def test_is_bored_single_letters():
    assert is_bored("I. I. I.") == 0

def test_is_bored_with_apostrophes():
    assert is_bored("I'm. I've. I'll.") == 0