# Test cases for HumanEval/153
# Generated using Claude API


def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """

    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans



# Generated test cases:
import pytest

@pytest.mark.parametrize("class_name,extensions,expected", [
    ("Strength", ["Extension"], "Strength.Extension"),
    ("MyClass", ["Hello", "World"], "MyClass.Hello"),
    ("Calculator", ["UPPER", "lower"], "Calculator.UPPER"),
    ("Test", ["ABCdef", "abcDEF"], "Test.ABCdef"),
    ("Complex", ["aA1b2B", "1A2b3C"], "Complex.1A2b3C"),
    ("Empty", ["test", ""], "Empty.test"),
    ("Special", ["A@B#C", "a$b%c"], "Special.A@B#C"),
    ("Mixed", ["Ab1Cd2Ef", "Ab2Cd3Ef"], "Mixed.Ab1Cd2Ef"),
    ("Class", ["ALLCAPS", "nocaps", "MixedCAPS"], "Class.ALLCAPS"),
    ("Test", ["a1B2c3", "A1b2C3", "123ABC"], "Test.123ABC")
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

def test_strongest_extension_single_extension():
    assert Strongest_Extension("Class", ["Test"]) == "Class.Test"

def test_strongest_extension_same_case_count():
    assert Strongest_Extension("Test", ["aAbB", "AaBb"]) == "Test.aAbB"

def test_strongest_extension_numbers_only():
    assert Strongest_Extension("Numbers", ["123", "456"]) == "Numbers.123"

@pytest.mark.parametrize("class_name,extensions", [
    ("", []),
    (None, ["test"]),
    ("Test", None),
    ("Test", [])
])
def test_strongest_extension_invalid_inputs(class_name, extensions):
    with pytest.raises(Exception):
        Strongest_Extension(class_name, extensions)

def test_strongest_extension_special_chars():
    assert Strongest_Extension("Special", ["@#$%", "!&*()"]) == "Special.@#$%"

def test_strongest_extension_whitespace():
    assert Strongest_Extension("Space", ["  A  ", " b "]) == "Space.  A  "

def test_strongest_extension_unicode():
    assert Strongest_Extension("Unicode", ["αβγ", "ΑΒΓ"]) == "Unicode.ΑΒΓ"

def test_strongest_extension_long_strings():
    assert Strongest_Extension("Long", ["AAAAAAaaaaaa", "BBBBBBbbbbbb"]) == "Long.AAAAAAaaaaaa"