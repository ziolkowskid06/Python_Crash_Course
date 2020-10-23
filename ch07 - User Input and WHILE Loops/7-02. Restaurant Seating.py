"""
Write a program that asks the user how many people are in their dinner group.
"""

seating = input('How many people are in your dinner group?\n')
seating = int(seating)
if seating > 8:
    print("You need to wait for a table.")
else:
    print("Table is ready!")
