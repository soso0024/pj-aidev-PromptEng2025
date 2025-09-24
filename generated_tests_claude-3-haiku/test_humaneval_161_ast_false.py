# Test cases for HumanEval/161
# Generated using Claude API


def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """

    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s


# Generated test cases:
import pytest

def test_solve_empty_string():
    assert solve('') == ''

def test_solve_all_uppercase():
    assert solve('HELLO') == 'hello'

def test_solve_all_lowercase():
    assert solve('hello') == 'HELLO'

def test_solve_mixed_case():
    assert solve('HeLlO') == 'hEllO'

def test_solve_non_alphabetic_characters():
    assert solve('H3ll0 W0rld!') == '!dlr0W 0ll3H'

@pytest.mark.parametrize("input,expected", [
    ('', ''),
    ('HELLO', 'hello'),
    ('hello', 'HELLO'),
    ('HeLlO', 'hEllO'),
    ('H3ll0 W0rld!', '!dlr0W 0ll3H')
])
def test_solve_with_parameterized_inputs(input, expected):
    assert solve(input) == expected

def solve(s):
    flg = 0
    idx = 0
    new_str = list(s)
    for i in new_str:
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    return ''.join(new_str) if flg else s[::-1]