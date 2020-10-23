"""
Modify your program from Exercise 6-2 so each person can have more than one favorite number.
"""

favorite_numbers = {
    'Anna': [22, 32],
    'Eva': [63, 54, 78],
    'Monica': [11, 2, 21, 99],
    'Elizabeth': [99, 88],
    'Kristien': [12, 100, 1, 0, 10],
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name} likes these numbers:")
    for number in numbers:
        print(f"\t{number}")
