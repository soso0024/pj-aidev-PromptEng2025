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

class TestBf:
    
    def test_adjacent_planets_forward(self):
        assert bf("Mercury", "Venus") == ()
        assert bf("Venus", "Earth") == ()
        assert bf("Earth", "Mars") == ()
        assert bf("Mars", "Jupiter") == ()
        assert bf("Jupiter", "Saturn") == ()
        assert bf("Saturn", "Uranus") == ()
        assert bf("Uranus", "Neptune") == ()
    
    def test_adjacent_planets_backward(self):
        assert bf("Venus", "Mercury") == ()
        assert bf("Earth", "Venus") == ()
        assert bf("Mars", "Earth") == ()
        assert bf("Jupiter", "Mars") == ()
        assert bf("Saturn", "Jupiter") == ()
        assert bf("Uranus", "Saturn") == ()
        assert bf("Neptune", "Uranus") == ()
    
    def test_same_planet(self):
        assert bf("Mercury", "Mercury") == ()
        assert bf("Venus", "Venus") == ()
        assert bf("Earth", "Earth") == ()
        assert bf("Mars", "Mars") == ()
        assert bf("Jupiter", "Jupiter") == ()
        assert bf("Saturn", "Saturn") == ()
        assert bf("Uranus", "Uranus") == ()
        assert bf("Neptune", "Neptune") == ()
    
    def test_planets_with_one_between_forward(self):
        assert bf("Mercury", "Earth") == ("Venus",)
        assert bf("Venus", "Mars") == ("Earth",)
        assert bf("Earth", "Jupiter") == ("Mars",)
        assert bf("Mars", "Saturn") == ("Jupiter",)
        assert bf("Jupiter", "Uranus") == ("Saturn",)
        assert bf("Saturn", "Neptune") == ("Uranus",)
    
    def test_planets_with_one_between_backward(self):
        assert bf("Earth", "Mercury") == ("Venus",)
        assert bf("Mars", "Venus") == ("Earth",)
        assert bf("Jupiter", "Earth") == ("Mars",)
        assert bf("Saturn", "Mars") == ("Jupiter",)
        assert bf("Uranus", "Jupiter") == ("Saturn",)
        assert bf("Neptune", "Saturn") == ("Uranus",)
    
    def test_planets_with_multiple_between_forward(self):
        assert bf("Mercury", "Mars") == ("Venus", "Earth")
        assert bf("Venus", "Jupiter") == ("Earth", "Mars")
        assert bf("Earth", "Saturn") == ("Mars", "Jupiter")
        assert bf("Mars", "Uranus") == ("Jupiter", "Saturn")
        assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    
    def test_planets_with_multiple_between_backward(self):
        assert bf("Mars", "Mercury") == ("Venus", "Earth")
        assert bf("Jupiter", "Venus") == ("Earth", "Mars")
        assert bf("Saturn", "Earth") == ("Mars", "Jupiter")
        assert bf("Uranus", "Mars") == ("Jupiter", "Saturn")
        assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    
    def test_far_apart_planets_forward(self):
        assert bf("Mercury", "Jupiter") == ("Venus", "Earth", "Mars")
        assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")
        assert bf("Earth", "Uranus") == ("Mars", "Jupiter", "Saturn")
        assert bf("Mars", "Neptune") == ("Jupiter", "Saturn", "Uranus")
    
    def test_far_apart_planets_backward(self):
        assert bf("Jupiter", "Mercury") == ("Venus", "Earth", "Mars")
        assert bf("Saturn", "Venus") == ("Earth", "Mars", "Jupiter")
        assert bf("Uranus", "Earth") == ("Mars", "Jupiter", "Saturn")
        assert bf("Neptune", "Mars") == ("Jupiter", "Saturn", "Uranus")
    
    def test_extreme_cases_forward(self):
        assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
        assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
        assert bf("Venus", "Neptune") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    
    def test_extreme_cases_backward(self):
        assert bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
        assert bf("Uranus", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
        assert bf("Neptune", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    
    def test_invalid_planet_names(self):
        assert bf("Pluto", "Earth") == ()
        assert bf("Earth", "Pluto") == ()
        assert bf("Pluto", "Moon") == ()
        assert bf("Sun", "Mercury") == ()
        assert bf("Mars", "Sun") == ()
    
    def test_empty_strings(self):
        assert bf("", "Earth") == ()
        assert bf("Mars", "") == ()
        assert bf("", "") == ()
    
    def test_case_sensitivity(self):
        assert bf("mercury", "Venus") == ()
        assert bf("Mercury", "venus") == ()
        assert bf("MERCURY", "VENUS") == ()
        assert bf("earth", "mars") == ()
    
    def test_none_values(self):
        assert bf(None, "Earth") == ()
        assert bf("Mars", None) == ()
        assert bf(None, None) == ()
    
    @pytest.mark.parametrize("planet1,planet2,expected", [
        ("Mercury", "Venus", ()),
        ("Mercury", "Earth", ("Venus",)),
        ("Mercury", "Mars", ("Venus", "Earth")),
        ("Venus", "Mars", ("Earth",)),
        ("Earth", "Jupiter", ("Mars",)),
        ("Mars", "Saturn", ("Jupiter",)),
        ("Jupiter", "Neptune", ("Saturn", "Uranus")),
        ("Neptune", "Jupiter", ("Saturn", "Uranus")),
        ("Saturn", "Venus", ("Earth", "Mars", "Jupiter")),
        ("Uranus", "Mercury", ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))
    ])
    def test_parametrized_valid_cases(self, planet1, planet2, expected):
        assert bf(planet1, planet2) == expected
    
    @pytest.mark.parametrize("planet1,planet2", [
        ("InvalidPlanet", "Earth"),
        ("Mars", "InvalidPlanet"),
        ("", "Venus"),
        ("Jupiter", ""),
        ("Mercury", "Mercury"),
        ("Earth", "Earth"),
        (None, "Mars"),
        ("Venus", None)
    ])
    def test_parametrized_invalid_cases(self, planet1, planet2):
        assert bf(planet1, planet2) == ()
