"""
Add an if test to make sure the list of users is not empty.
"""

names = []
if names:
    for name in names:
        print(f'Hello {name.title()}, thanks you for logging in again.')
else:
    print('We need more users!')
