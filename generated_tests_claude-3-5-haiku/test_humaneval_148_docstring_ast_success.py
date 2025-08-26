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

def test_bf_normal_cases():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()

def test_bf_adjacent_planets():
    assert bf("Mercury", "Venus") == ()
    assert bf("Venus", "Earth") == ()
    assert bf("Earth", "Mars") == ()

def test_bf_invalid_planets():
    assert bf("Pluto", "Mars") == ()
    assert bf("Mars", "Pluto") == ()
    assert bf("Sun", "Neptune") == ()
    assert bf("", "") == ()

def test_bf_case_sensitivity():
    assert bf("mercury", "Neptune") == ()
    assert bf("MERCURY", "Neptune") == ()

def test_bf_reverse_order():
    assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    assert bf("Uranus", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
