"""
Start with your program from Exercise 4-1 and make a copy of the list of pizzas.
"""

my_pizzas = ['margaritta', 'BBQ Chicken', 'havana', 'pepperoni']
friend_pizzas = my_pizzas[:]
# Add a new pizza to the original list
my_pizzas.append('four cheese')
print(f"Original list: \n{my_pizzas}\n\nFriend list: \n{friend_pizzas}\n\n")
# Add a new pizza to the friend list
friend_pizzas.append('new yourk')
print(f"Original list: \n{my_pizzas}\n\nFriend list: \n{friend_pizzas}\n")
