"""
Write an if-elif-else chain that determines a person’s stage of life.
"""

age = 65
if age < 2:
    print('The person is a baby.')
elif age < 4:
    print('The person is a toddler.')
elif age < 13:
    print('The person is a kid')
elif age < 20:
    print('The person is a teenager.')
elif age < 65:
    print('The person is an adult.')
elif age > 64:
    print('The person is an elder.')
