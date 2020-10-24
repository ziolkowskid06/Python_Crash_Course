"""
Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant.
"""

"""
create: restaurant.py
from restaurant import Restaurant as R
"""


class Restaurant:
    """Model of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Descriptionf of the restaurant"""
        print(f"The name of restaurant is '{self.restaurant_name}'.")
        print(f"\tThis is a '{self.cuisine_type}' restaurant.")

    def open_restaurant(self):
        """Inform restaurant is open"""
        print("\tYou are lucky. It's open now!")


"""
create: my_restaurant.py
from restaurant import Restaurant as R
"""

# Make restaurant instance and call the method
my_restaurant = R("Roma", "Italian")
my_restaurant.describe_restaurant()
