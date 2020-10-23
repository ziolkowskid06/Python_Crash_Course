"""
Write more conditional tests.
"""

# Equality and iequality with strings.
motorcycle = 'Ducati'
print("Is motorcycle != 'Ducati'? I predict False.")
print(motorcycle == 'ducati')
print("\nIs motorycle == 'Ducati'? I predict True.")
print(motorcycle == 'Ducati')
# Test using lower() method.
pc = 'DELL'
print("\n\nIs pc == 'dell'? I predict True.")
print(pc.lower() == 'dell')
# Check if item is in a list or not.
names = ['Anna', 'Julia', 'Rachel', 'Elizabeth']
print("\n\nCheck, if 'Samantha' is not in the list. I predict True.")
print('Samantha' not in names)
print("\nCheck, if 'Julia' is in the list. I preduct True.")
print('Julia' in names)
