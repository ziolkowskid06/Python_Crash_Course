"""
Make a class called Restaurant.
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


my_restaurant = Restaurant('victoria', 'spanish')
print(f"{my_restaurant.restaurant_name}")
print(f"{my_restaurant.cuisine_type}\n")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
