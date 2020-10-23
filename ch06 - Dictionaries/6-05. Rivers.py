"""
Make a dictionary containing three major rivers and the country each river runs through.
"""

rivers = {
    'nile': 'egypt',
    'wisla': 'poland',
    'arno': 'italy',
}
for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')
# Print rivers only.
for river in rivers.keys():
    print(f'{river.title()}')
# Print values only.
for country in rivers.values():
    print(f'{country.title()}')
