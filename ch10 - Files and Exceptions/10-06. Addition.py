"""
Common problem when prompting for numerical input occurs when people provide text instead of numbers.
"""

try:
    x = input("Enter the number: ")
    x = int(x)
    y = input("Enter the number: ")
    y = int(y)
except ValueError:
    print("Only numbers are accepted!")
else:
    sum = x + y
    print(f"The sum is: {sum}")
