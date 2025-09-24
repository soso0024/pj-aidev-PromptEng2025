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
from typing import List

def test_parse_music_empty_string():
    assert parse_music('') == []

def test_parse_music_single_note():
    assert parse_music('o') == [4]

def test_parse_music_multiple_notes():
    assert parse_music('o o| .|') == [4, 2, 1]

def test_parse_music_with_extra_spaces():
    assert parse_music('o  o|  .|') == [4, 2, 1]

def test_parse_music_invalid_note():
    with pytest.raises(KeyError):
        parse_music('o x')

@pytest.mark.parametrize("input,expected", [
    ('o', [4]),
    ('o o|', [4, 2]),
    ('o o| .|', [4, 2, 1]),
    ('', []),
    ('o x', pytest.raises(KeyError))
])
def test_parse_music_parametrized(input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            parse_music(input)
    else:
        assert parse_music(input) == expected