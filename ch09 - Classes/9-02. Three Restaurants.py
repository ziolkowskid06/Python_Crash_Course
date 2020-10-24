"""
Create three different instances from the class.
"""


class Restaurant:
    """Model of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Description of the restaurant"""
        print(f"The name of restaurant is '{self.restaurant_name}'.")
        print(f"\tThis is a '{self.cuisine_type}' restaurant.\n")

    def open_restaurant(self):
        """Inform restaurant is open"""
        print("\tYou are lucky. It's open now!\n")


# Create three instances
my_rest = Restaurant('alan', 'turkish')
my_rest.describe_restaurant()
my_rest2 = Restaurant('jashen', 'indian')
my_rest2.describe_restaurant()
my_rest3 = Restaurant('roma', 'italian')
my_rest3.describe_restaurant()
