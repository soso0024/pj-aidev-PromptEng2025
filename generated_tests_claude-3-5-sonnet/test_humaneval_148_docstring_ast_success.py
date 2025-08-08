# Test cases for HumanEval/148
# Generated using Claude API


def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''

    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    if planet1_index < planet2_index:
        return (planet_names[planet1_index + 1: planet2_index])
    else:
        return (planet_names[planet2_index + 1 : planet1_index])


# Generated test cases:
import pytest

@pytest.mark.parametrize("planet1,planet2,expected", [
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus",)),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Neptune", "Mars", ("Jupiter", "Saturn", "Uranus")),
    ("Mercury", "Mercury", ()),
    ("Earth", "Earth", ()),
    ("Invalid", "Mercury", ()),
    ("Mercury", "Invalid", ()),
    ("Invalid1", "Invalid2", ()),
    ("Mercury", "Venus", ()),
    ("Venus", "Mercury", ()),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Uranus", "Earth", ("Mars", "Jupiter", "Saturn")),
    ("Mars", "Saturn", ("Jupiter",)),
    ("Saturn", "Mars", ("Jupiter",))
])
def test_bf_parametrized(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected

def test_bf_case_sensitivity():
    assert bf("mercury", "Mars") == ()
    assert bf("MERCURY", "MARS") == ()
    assert bf("Mercury", "mars") == ()

def test_bf_empty_strings():
    assert bf("", "") == ()
    assert bf("Mercury", "") == ()
    assert bf("", "Mars") == ()

def test_bf_special_characters():
    assert bf("Mercury!", "Mars") == ()
    assert bf("Mars*", "Jupiter") == ()
    assert bf("Earth ", "Venus") == ()

def test_bf_none_input():
    assert bf(None, "Mars") == ()
    assert bf("Mars", None) == ()
    assert bf(None, None) == ()

def test_bf_numeric_input():
    assert bf(1, "Mars") == ()
    assert bf("Mars", 2) == ()
    assert bf(1, 2) == ()
