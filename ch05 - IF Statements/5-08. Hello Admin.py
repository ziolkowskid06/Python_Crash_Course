"""
Make a list of five or more usernames, including the name'admin'.
Imagine you are writing code that will print a greeting to each user after they log in to a website and the question for admin.
"""

names = ['anna', 'elizabeth', 'julia', 'kim', 'admin', 'rachel']
for name in names:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f"Hello {name.title()}, thank you for logging in again.")
