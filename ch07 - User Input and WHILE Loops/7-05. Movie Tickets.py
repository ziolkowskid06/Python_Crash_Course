"""
A movie theater charges different ticket prices depending on a person’s age.
"""

active = True
while active:
    ticket = input("\nHow old are you? Insert '0' to exit.\n")
    ticket = int(ticket)
    if ticket <= 0:
        active = False
    elif ticket < 3:
        print('The ticket is free!')
    elif ticket < 12:
        print('The ticket is $10.')
    elif ticket >= 12:
        print('The ticket is $15.')
