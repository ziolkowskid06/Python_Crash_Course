# Import choice function (return randomly chosen element)
from random import choice

# list of 10 numbers and 4 letters
tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd']

# select 4 element from the list
tickets_won = []
print("\nLet's make lottery:")
while len(tickets_won) < 4:
    winner = choice(tickets)
    tickets_won.append(winner)
    print(f"The winner is: {winner}")
    tickets.remove(winner)
print(f"\n4 prizes go to: {tickets_won}")
