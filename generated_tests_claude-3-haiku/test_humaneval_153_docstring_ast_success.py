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
    if not class_name or not isinstance(class_name, str):
        raise TypeError("class_name must be a non-empty string")
    if not extensions or not isinstance(extensions, list) or not all(isinstance(ext, str) for ext in extensions):
        raise TypeError("extensions must be a non-empty list of strings")

    strong = extensions[0] if extensions else "None"
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()]) if extensions else 0
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans

def test_strongest_extension_basic():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_equal_strength():
    assert Strongest_Extension('test', ['AA', 'BB', 'CC']) == 'test.AA'

def test_strongest_extension_empty_extensions():
    with pytest.raises(TypeError):
        Strongest_Extension('class', [])

def test_strongest_extension_single_extension():
    assert Strongest_Extension('class', ['extension']) == 'class.extension'

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension('class', ['abc', 'def', 'ghi']) == 'class.abc'

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension('class', ['ABC', 'DEF', 'GHI']) == 'class.ABC'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('class', ['AbC', 'dEf', 'gHi']) == 'class.AbC'

def test_strongest_extension_non_alphabetic_characters():
    assert Strongest_Extension('class', ['A1B', '2C3', 'D4E']) == 'class.A1B'

def test_strongest_extension_case_insensitive():
    assert Strongest_Extension('class', ['aBc', 'dEf', 'gHi']) == 'class.aBc'

def test_strongest_extension_empty_class_name():
    with pytest.raises(TypeError):
        Strongest_Extension('', ['AA', 'BB', 'CC'])

def test_strongest_extension_none_class_name():
    with pytest.raises(TypeError):
        Strongest_Extension(None, ['AA', 'BB', 'CC'])

def test_strongest_extension_none_extensions():
    with pytest.raises(TypeError):
        Strongest_Extension('class', None)