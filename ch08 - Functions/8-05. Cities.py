"""
Write a function called describe_city() that accepts the name of a city and its country.
"""


def describe_city(city, country='Poland'):
    """Print the city and its country."""
    print(f"{city.title()} is in {country.title()}.")


describe_city('Gdynia')
