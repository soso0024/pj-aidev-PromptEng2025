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

@pytest.mark.parametrize("input_str,expected", [
    ("hello", "HELLO"),
    ("WORLD", "world"),
    ("Hello World", "hELLO wORLD"),
    ("", ""),
    ("123", "321"),
    ("abc123", "ABC123"),
    ("!@#", "#@!"),
    ("MiXeD cAsE", "mIxEd CaSe"),
    ("Hello123World!", "hELLO123wORLD!"),
    ("    ", "    "),
    ("a", "A"),
    ("Z", "z"),
    ("12345!@#$%", "%$#@!54321"),
    ("Hello\nWorld", "hELLO\nwORLD"),
    ("Python3.9", "pYTHON3.9"),
    ("__init__", "__INIT__"),
    ("camelCase", "CAMELcASE"),
    ("Snake_case", "sNAKE_CASE"),
    ("12345", "54321"),
    ("!@#$%", "%$#@!"),
])
def test_solve(input_str, expected):
    assert solve(input_str) == expected

@pytest.mark.parametrize("input_str", [
    None,
    123,
    ["hello"],
    {"key": "value"},
    True,
    3.14
])
def test_solve_invalid_input(input_str):
    with pytest.raises((TypeError, AttributeError)):
        solve(input_str)

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_single_character():
    assert solve("a") == "A"
    assert solve("Z") == "z"
    assert solve("1") == "1"
    assert solve("!") == "!"

def test_solve_whitespace():
    assert solve("   ") == "   "
    assert solve("\t") == "\t"
    assert solve("\n") == "\n"

def test_solve_special_characters():
    assert solve("!@#$%^&*()") == ")(*&^%$#@!"
    assert solve("Hello!@#") == "hELLO!@#"

def test_solve_mixed_content():
    assert solve("Ab1@Cd2#Ef3") == "aB1@cD2#eF3"
    assert solve("12Ab34Cd56") == "12aB34cD56"