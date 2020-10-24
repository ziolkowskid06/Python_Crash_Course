"""
Write a program that prompts the user for their name.
"""

name = input("What's your name? ")

filename = 'guest.txt'

# Save the variable into the .txt file
with open(filename, 'w') as f:
    f.write(name)
