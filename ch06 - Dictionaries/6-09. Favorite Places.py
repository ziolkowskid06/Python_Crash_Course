"""
Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary,
and store one to three favorite places for each person.
"""

favorite_places = {
    'Eva': ['London', 'Paris'],
    'Sarah': ['Glasgow'],
    'Mary': ['Berlin', 'Moscow', 'Lisbona'],
}
for name, places in favorite_places.items():
    print(f'{name} visited following cities:')
    for place in places:
        print(f'\t-{place}')
    print('\n')
