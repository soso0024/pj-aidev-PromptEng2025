# Test cases for HumanEval/17
# Generated using Claude API

from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]


# Generated test cases:
import pytest
from typing import List

@pytest.mark.parametrize("music_string,expected", [
    ("o o| .|", [4, 2, 1]),
    ("o o o", [4, 4, 4]),
    ("o| o| o|", [2, 2, 2]),
    (".| .| .|", [1, 1, 1]),
    ("", []),
    ("   ", []),
    ("o", [4]),
    ("o|", [2]),
    (".|", [1]),
    ("o o| .| o", [4, 2, 1, 4]),
    ("  o  o|  .|  ", [4, 2, 1]),
])
def test_parse_music_valid_inputs(music_string: str, expected: List[int]):
    assert parse_music(music_string) == expected

@pytest.mark.parametrize("invalid_input", [
    "x",
    "o o x",
    "oo",
    "|",
    ".|o",
    "o||",
    "o o| .| x",
])
def test_parse_music_invalid_inputs(invalid_input: str):
    with pytest.raises(KeyError):
        parse_music(invalid_input)

def test_parse_music_none_input():
    with pytest.raises(AttributeError):
        parse_music(None)

def test_parse_music_wrong_type():
    with pytest.raises(AttributeError):
        parse_music(123)

def test_parse_music_empty_list():
    with pytest.raises(AttributeError):
        parse_music([])

def test_parse_music_empty_dict():
    with pytest.raises(AttributeError):
        parse_music({})
