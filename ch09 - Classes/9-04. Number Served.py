"""
Start with your program from Exercise 9-1.
"""


class Restaurant:
    """Model of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        """Enter, how many people have been served"""
        self.number_served = number

    def increment_number_served(self):
        """Increment number by 20"""
        self.number_served += 20

    def describe_restaurant(self):
        """Descriptionf of the restaurant"""
        print(f"\nThe name of restaurant is '{self.restaurant_name}'.")
        print(f"\tThis is a '{self.cuisine_type}' restaurant.")
        print(f"\t{self.number_served} customers have been served today.")

    def open_restaurant(self):
        """Inform restaurant is open"""
        print("\tYou are lucky. It's open now!")


my_rest = Restaurant('roma', 'italian')
my_rest.set_number_served(20)
my_rest.increment_number_served()
my_rest.describe_restaurant()
