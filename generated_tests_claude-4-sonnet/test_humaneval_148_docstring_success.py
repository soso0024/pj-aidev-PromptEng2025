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

def bf(planet1, planet2):
    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    if planet1_index < planet2_index:
        return (planet_names[planet1_index + 1: planet2_index])
    else:
        return (planet_names[planet2_index + 1 : planet1_index])

def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_adjacent_planets():
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Earth") == ()
    assert bf("Earth", "Mars") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()
    assert bf("Mars", "Mars") == ()

def test_bf_invalid_planet_names():
    assert bf("Pluto", "Earth") == ()
    assert bf("Mars", "Pluto") == ()
    assert bf("Pluto", "NotAPlanet") == ()

def test_bf_empty_strings():
    assert bf("", "Earth") == ()
    assert bf("Mars", "") == ()
    assert bf("", "") == ()

def test_bf_case_sensitive():
    assert bf("earth", "Mars") == ()
    assert bf("Earth", "mars") == ()
    assert bf("EARTH", "MARS") == ()

def test_bf_reverse_order():
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    assert bf("Uranus", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_all_planets_between():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

@pytest.mark.parametrize("planet1,planet2,expected", [
    ("Venus", "Mars", ("Earth",)),
    ("Mars", "Venus", ("Earth",)),
    ("Saturn", "Neptune", ("Uranus",)),
    ("Neptune", "Saturn", ("Uranus",)),
    ("Mercury", "Mars", ("Venus", "Earth")),
    ("Jupiter", "Uranus", ("Saturn",)),
])
def test_bf_parametrized(planet1, planet2, expected):
    assert bf(planet1, planet2) == expected

def test_bf_return_type():
    result = bf("Earth", "Jupiter")
    assert isinstance(result, tuple)

def test_bf_empty_result_type():
    result = bf("InvalidPlanet", "Earth")
    assert isinstance(result, tuple)
    assert len(result) == 0
