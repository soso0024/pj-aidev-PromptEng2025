# Test cases for HumanEval/23
# Generated using Claude API



def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    return len(string)


# Generated test cases:
import pytest

@pytest.mark.parametrize("input,expected", [
    ("", 0),
    ("abc", 3),
    ("hello world", 11),
    ("   ", 3),
    ("\n\t", 2),
    ("🤖", 1),
    (123, TypeError),
    (None, TypeError)
])
def test_strlen(input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            strlen(input)
    else:
        assert strlen(input) == expected
