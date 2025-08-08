# Test cases for HumanEval/101
# Generated using Claude API


def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()


# Generated test cases:
import pytest

def words_string(s):
    if not s:
        return []

    words = []
    current_word = ""
    for char in s:
        if char == ",":
            if current_word:
                words.append(current_word.strip())
                current_word = ""
        else:
            current_word += char
    if current_word:
        words.append(current_word.strip())
    return words

def test_words_string_empty_string():
    assert words_string('') == []

def test_words_string_single_word():
    assert words_string('hello') == ['hello']

def test_words_string_multiple_words():
    assert words_string('hello, world, python') == ['hello', 'world', 'python']

def test_words_string_leading_trailing_spaces():
    assert words_string('  hello, world, python  ') == ['hello', 'world', 'python']

def test_words_string_consecutive_commas():
    assert words_string('hello,,world,python') == ['hello', 'world', 'python']

@pytest.mark.parametrize("input,expected", [
    ('', []),
    ('hello', ['hello']),
    ('hello, world, python', ['hello', 'world', 'python']),
    ('  hello, world, python  ', ['hello', 'world', 'python']),
    ('hello,,world,python', ['hello', 'world', 'python'])
])
def test_words_string_parametrized(input, expected):
    assert words_string(input) == expected

def test_words_string_type_error():
    with pytest.raises(TypeError):
        words_string(123)