"""
Replace your series of print() calls with a loop that runs through the dictionary’s keys and values.
"""

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}
for key, value in glossary.items():
    print(f'{key.title()}: {value}\n')
