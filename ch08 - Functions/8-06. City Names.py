"""
Write a function called city_country() that takes in the name of a city and its country.
The function should return a string.
"""


def city_country(city, country):
    """Print sentence"""
    sentence = (f"{city.title()}, {country.title()}.")
    return print(sentence)


city_country("Gdynia", "Poland")
