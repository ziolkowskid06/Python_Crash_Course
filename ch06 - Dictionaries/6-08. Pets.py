"""
Make several dictionaries, where each dictionary represents a different pet.
"""

pets = []
pet = {'kind': 'cat', 'owner': 'eva'}
pets.append(pet)
pet = {'kind': 'dog', 'owner': 'rachel'}
pets.append(pet)
pet = {'kind': 'hamster', 'owner': 'anna'}
pets.append(pet)
pet = {'kind': 'rabbit', 'owner': 'sarah'}
pets.append(pet)
for pet in pets:
    kind = f"{pet['kind']}"
    owner = f"{pet['owner'].title()}"
    print(f" This is {owner}'s {kind}!")
