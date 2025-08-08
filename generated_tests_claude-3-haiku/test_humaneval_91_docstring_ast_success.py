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

def test_is_bored_empty_string():
    assert is_bored("") == 0

def test_is_bored_no_boredoms():
    assert is_bored("Hello world") == 0

def test_is_bored_single_boredom():
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1

def test_is_bored_multiple_boredoms():
    assert is_bored("I am bored. I want to go home. I need a nap. I like pizza.") == 4

def test_is_bored_boredom_in_middle():
    assert is_bored("The weather is nice. I am feeling good. Let's go for a walk.") == 1

def test_is_bored_boredom_at_end():
    assert is_bored("The day was long. I am tired.") == 1

def test_is_bored_boredom_with_punctuation():
    assert is_bored("I am bored! I want to go home? I need a nap.") == 3

def test_is_bored_boredom_with_capitalization():
    assert is_bored("I am Bored. I want to go home. I need a Nap.") == 3

@pytest.mark.parametrize("input,expected", [
    ("", 0),
    ("Hello world", 0),
    ("The sky is blue. The sun is shining. I love this weather", 1),
    ("I am bored. I want to go home. I need a nap. I like pizza.", 4),
    ("The weather is nice. I am feeling good. Let's go for a walk.", 1),
    ("The day was long. I am tired.", 1),
    ("I am bored! I want to go home? I need a nap.", 3),
    ("I am Bored. I want to go home. I need a Nap.", 3)
])
def test_is_bored_parametrized(input, expected):
    assert is_bored(input) == expected
