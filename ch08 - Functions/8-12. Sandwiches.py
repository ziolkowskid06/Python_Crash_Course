"""
Write a function that accepts a list of items a person wants on a sandwich.
"""


def make_sandwich(*toppings):
    """Show a lits of items a person wants on sandwich"""
    print("Summary of sandwich:")
    for topping in toppings:
        print(f"\t- {topping}")


make_sandwich('ham', 'cheese', 'onion', 'tomato', 'salami')
