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
import re

def is_bored(S):
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence.strip().startswith('I ') for sentence in sentences)

def test_is_bored_empty_string():
    assert is_bored("") == 0

def test_is_bored_no_boredoms():
    assert is_bored("Hello world.") == 0

def test_is_bored_single_boredom():
    assert is_bored("I am bored. The weather is nice.") == 1

def test_is_bored_multiple_boredoms():
    assert is_bored("I am bored. I want to go outside. The sky is blue.") == 2

def test_is_bored_boredom_in_middle():
    assert is_bored("The weather is nice. I am bored. Let's go for a walk.") == 1

def test_is_bored_boredom_at_end():
    assert is_bored("The sky is blue. I am bored.") == 1

def test_is_bored_boredom_with_punctuation():
    assert is_bored("I am bored! The weather is nice.") == 1

def test_is_bored_boredom_with_capitalization():
    assert is_bored("I Am Bored. The weather is nice.") == 1

def test_is_bored_multiple_sentences_with_boredoms():
    assert is_bored("I am bored. The weather is nice. I want to go outside.") == 2

def test_is_bored_boredom_with_extra_spaces():
    assert is_bored("I   am   bored. The weather is nice.") == 1

def test_is_bored_boredom_with_newline():
    assert is_bored("I am bored.\nThe weather is nice.") == 1

def test_is_bored_boredom_with_tab():
    assert is_bored("I\tam\tbored. The weather is nice.") == 1

def test_is_bored_boredom_with_multiple_punctuation():
    assert is_bored("I am bored!? The weather is nice.") == 1

def test_is_bored_boredom_with_multiple_sentences():
    assert is_bored("I am bored. The weather is nice. I want to go outside. I am so bored.") == 3

def test_is_bored_boredom_with_mixed_punctuation():
    assert is_bored("I am bored! The weather is nice. I want to go outside?") == 2

def test_is_bored_boredom_with_capitalized_i():
    assert is_bored("I Am Bored. The weather is nice.") == 1

def test_is_bored_boredom_with_lowercase_i():
    assert is_bored("i am bored. The weather is nice.") == 1

def test_is_bored_boredom_with_multiple_spaces():
    assert is_bored("I   am   bored.   The   weather   is   nice.") == 1

def test_is_bored_boredom_with_leading_spaces():
    assert is_bored("  I am bored. The weather is nice.") == 1

def test_is_bored_boredom_with_trailing_spaces():
    assert is_bored("I am bored.  The weather is nice.  ") == 1

def test_is_bored_boredom_with_multiple_sentences_and_punctuation():
    assert is_bored("I am bored! The weather is nice. I want to go outside? I am so bored.") == 3

def test_is_bored_boredom_with_multiple_sentences_and_mixed_punctuation():
    assert is_bored("I am bored! The weather is nice. I want to go outside? I am so bored.") == 3

def test_is_bored_boredom_with_multiple_sentences_and_capitalization():
    assert is_bored("I Am Bored. The Weather Is Nice. I Want To Go Outside. I Am So Bored.") == 4

def test_is_bored_boredom_with_multiple_sentences_and_mixed_case():
    assert is_bored("I am bored. The weather is nice. I Want To Go Outside. I am so bored.") == 3

def test_is_bored_boredom_with_multiple_sentences_and_extra_spaces():
    assert is_bored("I   am   bored.   The   weather   is   nice.   I   want   to   go   outside.   I   am   so   bored.") == 4

def test_is_bored_boredom_with_multiple_sentences_and_newlines():
    assert is_bored("I am bored.\nThe weather is nice.\nI want to go outside.\nI am so bored.") == 4

def test_is_bored_boredom_with_multiple_sentences_and_tabs():
    assert is_bored("I\tam\tbored.\tThe\tweather\tis\tnice.\tI\twant\tto\tgo\toutside.\tI\tam\tso\tbored.") == 4

def test_is_bored_boredom_with_multiple_sentences_and_mixed_punctuation_and_capitalization():
    assert is_bored("I Am Bored! The Weather Is Nice? I Want To Go Outside. I Am So Bored!") == 4

def test_is_bored_boredom_with_multiple_sentences_and_mixed_punctuation_and_capitalization_and_spaces():
    assert is_bored("  I   Am   Bored!   The   Weather   Is   Nice?   I   Want   To   Go   Outside.   I   Am   So   Bored!  ") == 4