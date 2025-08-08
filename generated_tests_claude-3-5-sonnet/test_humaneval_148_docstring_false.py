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

def test_bf_normal_order():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Jupiter") == ("Mars",)
    assert bf("Mercury", "Mars") == ("Venus", "Earth")

def test_bf_reverse_order():
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    assert bf("Mars", "Mercury") == ("Venus", "Earth")
    assert bf("Uranus", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn")

def test_bf_adjacent_planets():
    assert bf("Mercury", "Venus") == ()
    assert bf("Earth", "Mars") == ()
    assert bf("Saturn", "Uranus") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()
    assert bf("Mars", "Mars") == ()

def test_bf_invalid_planets():
    assert bf("Earth", "Pluto") == ()
    assert bf("Sun", "Mars") == ()
    assert bf("", "Mars") == ()
    assert bf("Earth", "") == ()
    assert bf("Invalid", "NotAPlanet") == ()

@pytest.mark.parametrize("planet1,planet2,expected", [
    ("Mercury", "Neptune", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Neptune", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")),
    ("Venus", "Saturn", ("Earth", "Mars", "Jupiter")),
    ("Mars", "Venus", ("Earth",)),
    ("Jupiter", "Mars", ("Earth", "Mars")),
])
def test_bf_parametrized(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected

@pytest.mark.parametrize("planet1,planet2", [
    ("Earth", None),
    (None, "Mars"),
    (123, "Mars"),
    ("Earth", 123),
    (None, None),
])
def test_bf_invalid_types(planet1, planet2):
    assert bf(planet1, planet2) == ()