# Test cases for HumanEval/48
# Generated using Claude API



def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """

    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


# Generated test cases:
from main import is_palindrome
import pytest

@pytest.mark.parametrize("input,expected", [
    ("", True),
    ("aba", True),
    ("aaaaa", True),
    ("zbcd", False),
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("Was it a car or a cat I saw?", True),
    ("Madam, in Eden, I'm Adam", True),
    ("Step on no pets", True),
    ("Taco cat", True),
    ("Borrow or rob?", True),
    ("Eva, can I see bees in a cave?", True),
    ("Yo, banana boy!", True),
    ("Dammit I'm mad.", True),
    ("Able was I ere I saw Elba", True),
    ("A Toyota's a Toyota", True),
    ("Borrow or rob?", True),
    ("Sit on a potato pan, Otis", True),
    ("Cigar? Toss it in a can. It is so tragic.", True),
    ("Do geese see God?", True),
    ("My gym", False),
    ("Rats live on no evil star", True),
    ("Harrah's casino", False),
    ("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama", True),
    ("Yo, banana boy!", True),
    ("Dammit I'm mad.", True),
    ("Able was I ere I saw Elba", True),
    ("A Toyota's a Toyota", True),
    ("Borrow or rob?", True),
    ("Sit on a potato pan, Otis", True),
    ("Cigar? Toss it in a can. It is so tragic.", True),
    ("Do geese see God?", True),
    ("My gym", False),
    ("Rats live on no evil star", True),
    ("Harrah's casino", False),
    ("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama", True),
])
def test_is_palindrome(input, expected):
    assert is_palindrome(input) == expected