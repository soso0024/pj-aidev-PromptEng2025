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

@pytest.mark.parametrize("input_str, expected", [
    ("Hello World", "hELLO wORLD"),
    ("Python", "pYTHON"),
    ("123abc456", "123ABC456"),
    ("", ""),
    ("   ", "   "),
    ("ABC123", "abc123"),
    ("HELLO WORLD", "hELLO wORLD"),
    ("hello WORLD", "HELLO world"),
    ("HeLlO wOrLd", "hELlO WORld"),
    ("1234567890", "1234567890"),
])
def test_solve(input_str, expected):
    assert solve(input_str) == expected

def test_solve_reverse():
    assert solve("123") == "321"
    assert solve("abc") == "cba"
    assert solve("   ") == "   "
    assert solve("") == ""

def test_solve_error():
    with pytest.raises(TypeError):
        solve(123)
    with pytest.raises(TypeError):
        solve(None)