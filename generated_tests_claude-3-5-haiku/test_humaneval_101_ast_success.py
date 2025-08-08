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

    s_list = []
    current_word = []
    
    for letter in s:
        if letter == ',':
            if current_word:
                s_list.append(''.join(current_word).strip())
                current_word = []
        elif letter.isspace() and current_word and current_word[-1] != ' ':
            current_word.append(' ')
        else:
            current_word.append(letter)
    
    if current_word:
        s_list.append(''.join(current_word).strip())
    
    return s_list

def test_words_string_empty_input():
    assert words_string('') == []

def test_words_string_single_word():
    assert words_string('hello') == ['hello']

def test_words_string_multiple_words():
    assert words_string('hello,world,python') == ['hello', 'world', 'python']

def test_words_string_with_spaces():
    assert words_string('hello, world, python') == ['hello', 'world', 'python']

def test_words_string_multiple_consecutive_commas():
    assert words_string('hello,,world') == ['hello', 'world']

def test_words_string_leading_trailing_commas():
    assert words_string(',hello,world,') == ['hello', 'world']

def test_words_string_complex_input():
    assert words_string('one,two three,four,five six') == ['one', 'two three', 'four', 'five six']

@pytest.mark.parametrize("input_str,expected", [
    ('', []),
    ('hello', ['hello']),
    ('hello,world', ['hello', 'world']),
    ('hello, world, python', ['hello', 'world', 'python']),
    (',test,', ['test']),
    ('multiple,,commas', ['multiple', 'commas'])
])
def test_words_string_parametrized(input_str, expected):
    assert words_string(input_str) == expected