"""
Write a while loop that asks people why they like programming.
"""

filename = 'programming_poll.txt'
responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)
    continue_poll = input("Would you like to let someone else respons? (y/n) ")
    if continue_poll == 'n':
        break
with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")
