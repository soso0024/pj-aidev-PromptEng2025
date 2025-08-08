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

def Strongest_Extension(class_name, extensions):
    if not extensions:
        raise IndexError("Extensions list cannot be empty")

    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val or (val == my_val and extensions.index(s) < extensions.index(strong)):
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans

def test_strongest_extension_basic():
    assert Strongest_Extension("MyClass", ["A", "B", "C"]) == "MyClass.A"

def test_strongest_extension_uppercase_count():
    assert Strongest_Extension("MyClass", ["AAA", "aa", "BB"]) == "MyClass.AAA"

def test_strongest_extension_mixed_case():
    assert Strongest_Extension("MyClass", ["aA", "Bb", "cC"]) == "MyClass.aA"

def test_strongest_extension_single_extension():
    assert Strongest_Extension("MyClass", ["Hello"]) == "MyClass.Hello"

def test_strongest_extension_complex_strings():
    assert Strongest_Extension("MyClass", ["ABCdef", "abcDEF", "AbCdEf"]) == "MyClass.ABCdef"

def test_strongest_extension_empty_extensions():
    with pytest.raises(IndexError):
        Strongest_Extension("MyClass", [])

@pytest.mark.parametrize("class_name,extensions,expected", [
    ("MyClass", ["AAA", "aa", "BB"], "MyClass.AAA"),
    ("DataModel", ["hello", "WORLD", "Python"], "DataModel.WORLD"),
    ("Service", ["a1B2c3", "A1b2C3", "1Abc2"], "Service.a1B2c3")
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected