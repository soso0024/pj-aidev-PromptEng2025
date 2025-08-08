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

def test_Strongest_Extension_empty_extensions():
    with pytest.raises(IndexError):
        Strongest_Extension("MyClass", [])

def test_Strongest_Extension_single_extension():
    assert Strongest_Extension("MyClass", ["ABC123"]) == "MyClass.ABC123"

def test_Strongest_Extension_multiple_extensions():
    assert Strongest_Extension("MyClass", ["ABC123", "DEF456", "GHI789"]) == "MyClass.ABC123"
    assert Strongest_Extension("MyClass", ["abc123", "DEF456", "GHI789"]) == "MyClass.DEF456"
    assert Strongest_Extension("MyClass", ["abc123", "def456", "GHI789"]) == "MyClass.GHI789"

def test_Strongest_Extension_all_lowercase():
    assert Strongest_Extension("MyClass", ["abc123", "def456", "ghi789"]) == "MyClass.abc123"

def test_Strongest_Extension_all_uppercase():
    assert Strongest_Extension("MyClass", ["ABC123", "DEF456", "GHI789"]) == "MyClass.ABC123"

def test_Strongest_Extension_mixed_case():
    assert Strongest_Extension("MyClass", ["Abc123", "dEf456", "gHi789"]) == "MyClass.Abc123"

def test_Strongest_Extension_non_alphabetic_characters():
    assert Strongest_Extension("MyClass", ["ABC123_", "DEF456!", "GHI789@"]) == "MyClass.ABC123_"
    assert Strongest_Extension("MyClass", ["abc123_", "DEF456!", "GHI789@"]) == "MyClass.DEF456!"
    assert Strongest_Extension("MyClass", ["abc123_", "def456!", "GHI789@"]) == "MyClass.GHI789@"

def test_Strongest_Extension_single_character_extensions():
    assert Strongest_Extension("MyClass", ["A", "b", "C"]) == "MyClass.A"
    assert Strongest_Extension("MyClass", ["a", "B", "c"]) == "MyClass.B"

def test_Strongest_Extension_case_insensitive_comparison():
    assert Strongest_Extension("MyClass", ["abc", "DEF", "ghi"]) == "MyClass.DEF"
    assert Strongest_Extension("MyClass", ["ABC", "def", "GHI"]) == "MyClass.ABC"

def test_Strongest_Extension_non_string_extensions():
    with pytest.raises(TypeError):
        Strongest_Extension("MyClass", [123, 456.789, True])

def Strongest_Extension(class_name, extensions):
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans
