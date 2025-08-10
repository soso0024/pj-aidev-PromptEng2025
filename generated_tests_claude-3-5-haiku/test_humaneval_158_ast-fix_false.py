# Test cases for HumanEval/158
# Generated using Claude API


def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    return sorted(words, key = lambda x: (-len(set(x)), x))[0]


# Generated test cases:
import pytest

def test_find_max_basic_case():
    assert find_max(["hello", "world", "python"]) == "python"

def test_find_max_same_length_different_chars():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_find_max_unique_chars():
    assert find_max(["abcde", "fghij", "klmno"]) == "abcde"

def test_find_max_repeated_chars():
    assert find_max(["aaa", "bbb", "abcde"]) == "abcde"

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

@pytest.mark.parametrize("words,expected", [
    (["hello", "world", "python"], "python"),
    (["abc", "def", "ghi"], "abc"),
    (["aaa", "bbb", "abcde"], "abcde"),
    (["unique", "chars", "test"], "unique")
])
def test_find_max_parametrized(words, expected):
    assert find_max(words) == expected

def test_find_max_empty_list():
    with pytest.raises(IndexError):
        find_max([])

def test_find_max_non_string_input():
    with pytest.raises(TypeError):
        find_max([1, 2, 3])

def test_find_max_mixed_types():
    with pytest.raises(TypeError):
        find_max(["hello", 123, "world"])