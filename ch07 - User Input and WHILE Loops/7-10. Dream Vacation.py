"""
Write a program that polls users about their dream vacation.
"""

poll = {}
while True:
    name = input("What's your name? ")
    vacation = input("If you could visit one place in the world, "
                     "where would you go? ")
    poll[name] = vacation
    quit = input("Stop asking? (yes/no) ")
    if quit == 'yes':
        break
print("\n---- Poll Result ----")
for name, vacation in poll.items():
    print(f"{name.title()} would go to {vacation.title()}.")
