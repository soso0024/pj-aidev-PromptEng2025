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

def test_planets_between_jupiter_and_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_planets_between_earth_and_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_planets_between_mercury_and_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_planets_between_uranus_and_mercury():
    assert bf("Uranus", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_same_planet_returns_empty_tuple():
    assert bf("Earth", "Earth") == ()

def test_invalid_planet_names():
    assert bf("Pluto", "Mars") == ()
    assert bf("Mars", "Pluto") == ()
    assert bf("Sun", "Neptune") == ()

def test_adjacent_planets():
    assert bf("Venus", "Earth") == ()
    assert bf("Earth", "Mars") == ()

def test_case_sensitivity():
    assert bf("mercury", "Neptune") == ()
    assert bf("Mercury", "neptune") == ()

def test_reverse_order_planets():
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
