# Test cases for HumanEval/119
# Generated using Claude API


def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''

    def check(s):
        val = 0
        for i in s:
            if i == '(':
                val = val + 1
            else:
                val = val - 1
            if val < 0:
                return False
        return True if val == 0 else False

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    return 'Yes' if check(S1) or check(S2) else 'No'


# Generated test cases:
import pytest

@pytest.mark.parametrize("input,expected", [
    (['()', ')'], 'Yes'),
    ([')', ')'], 'No'),
    (['(((', ')'], 'Yes'),
    (['(', '('], 'No'),
    (['(', ')()'], 'Yes'),
    (['(())', '()'], 'Yes'),
    (['(())', '('], 'No'),
    (['(', ')'], 'Yes'),
    (['(', ''], 'No'),
    (['', ')'], 'No'),
    (['(', '('], 'No'),
    (['(())', '())'], 'No'),
    (['(())', '(())'], 'Yes'),
    (['(())', '(()'], 'No'),
    (['(())', ')()'], 'No'),
    (['(())', '()('], 'No'),
    (['(())', '())()'], 'No'),
    (['(())', '(()()'], 'Yes'),
    (['(())', '(())()'], 'Yes'),
    (['(())', '((()))'], 'Yes'),
    (['(())', '(())('], 'No'),
    (['(())', '(())()'], 'Yes')
])
def test_match_parens(input, expected):
    def match_parens(lst):
        def check(s):
            val = 0
            for i in s:
                if i == '(':
                    val += 1
                else:
                    val -= 1
                if val < 0:
                    return False
            return val == 0

        S1 = ''.join(lst)
        S2 = lst[1] + lst[0]
        return 'Yes' if check(S1) or check(S2) else 'No'

    assert match_parens(input) == expected