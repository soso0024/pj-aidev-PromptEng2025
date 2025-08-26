# Test cases for HumanEval/118
# Generated using Claude API


def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """

    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return ""


# Generated test cases:
import pytest

def get_closest_vowel(word):
    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return ""

def test_get_closest_vowel_normal_cases():
    assert get_closest_vowel("hello") == "o"
    assert get_closest_vowel("rhythm") == ""
    assert get_closest_vowel("python") == "o"

def test_get_closest_vowel_edge_cases():
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("aaa") == ""

def test_get_closest_vowel_multiple_vowels():
    assert get_closest_vowel("beautiful") == "u"
    assert get_closest_vowel("queue") == "u"

def test_get_closest_vowel_case_sensitivity():
    assert get_closest_vowel("AbcdE") == "E"
    assert get_closest_vowel("HELLO") == "O"

@pytest.mark.parametrize("word,expected", [
    ("hello", "o"),
    ("rhythm", ""),
    ("python", "o"),
    ("", ""),
    ("a", ""),
    ("ab", ""),
    ("beautiful", "u"),
    ("queue", "u"),
    ("AbcdE", "E"),
    ("HELLO", "O")
])
def test_get_closest_vowel_parametrized(word, expected):
    assert get_closest_vowel(word) == expected