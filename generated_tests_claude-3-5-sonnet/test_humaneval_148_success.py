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
    ("Earth", "Jupiter", ("Mars",)),
    ("Jupiter", "Earth", ("Mars",)),
    ("Mercury", "Mars", ("Venus", "Earth")),
    ("Mars", "Mercury", ("Venus", "Earth")),
    ("Neptune", "Jupiter", ("Saturn", "Uranus")),
    ("Mercury", "Mercury", ()),
    ("Earth", "Earth", ()),
    ("Invalid", "Mars", ()),
    ("Mars", "Invalid", ()),
    ("Mercury", "Venus", ()),
    ("Venus", "Mercury", ()),
    ("Uranus", "Neptune", ()),
    ("Neptune", "Uranus", ()),
])
def test_bf_parametrized(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected

def test_bf_adjacent_planets():
    assert bf("Earth", "Mars") == ()
    assert bf("Mars", "Earth") == ()

def test_bf_distant_planets():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_invalid_inputs():
    assert bf("", "") == ()
    assert bf(None, "Mars") == ()
    assert bf("Mars", None) == ()
    assert bf("", "Mars") == ()
    assert bf("Mars", "") == ()

def test_bf_case_sensitivity():
    assert bf("earth", "Mars") == ()
    assert bf("MARS", "Jupiter") == ()
