"""
Add more peaple to the guest book.
"""

filename = 'guest_book.txt'

print("Enter 'q' when you are finished")
while True:
    name = input("\nWhat is your name? ")
    if name == 'q':
        break
    else:
        # Add person
        with open(filename, 'a') as f:
            f.write(f"{name.title()}\n")
        print(f"Hi {name.title()}, you have been added to the guest book.")
