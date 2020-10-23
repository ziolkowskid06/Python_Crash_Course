"""
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
"""

while True:
    topping = input("\nPlease insert a pizza toppinng. Enter 'quit' to exit.\n")
    if topping == 'quit':
        break
    else:
        print(f"{topping.title()} added to the pizza.")
