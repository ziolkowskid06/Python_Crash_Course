"""
Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
"""

person_1 = {'name': 'salma', 'last_name': 'hayek', 'location': 'mexico'}
person_2 = {'name': 'gamma', 'last_name': 'atkinson', 'location': 'los angeles'}
person_3 = {'name': 'elizabeth', 'last_name': 'hurtley', 'location': 'london'}
people = [person_1, person_2, person_3]
for person in people:
    print(f"{person['name'].title()} {person['last_name'].title()} "
          f"is living in {person['location'].title()}.")
