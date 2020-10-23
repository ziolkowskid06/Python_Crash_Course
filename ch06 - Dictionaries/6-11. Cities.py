"""
Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
Create a dictionary of information about each city.
"""

cities = {
    'gdynia': {
        'location': 'poland',
        'population': 300_000,
        'fact': 'the best',
    },
    'sao paulo': {
        'location': 'brasil',
        'population': 25_000_000,
        'fact': 'the most densed',
    },
    'paisley': {
        'location': 'united kingdom',
        'population': 75_000,
        'fact': 'the strangest',
    },
}
for city, city_info in cities.items():
    location = city_info['location'].title()
    population = city_info['population']
    fact = city_info['fact']
    print(f"\n{city.title()} is in {location}.")
    print(f"\tOver {population} peaple are living there.")
    print(f"\tThis is {fact} city!")
