"""
An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1.
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


class IceCreamStand(Restaurant):
    """Represent the ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        """
        Initalize attributes of the parent class.
        Add flavors list.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Show flavors"""
        print("\nThis ice cream has following flavors: ")
        for flavor in self.flavors:
            print(f"\t- {flavor}")


# Create instance for IceCreamStand and call its methd
stand = IceCreamStand('Cone')
stand.flavors = ['vanilla', 'mint', 'chocolate', 'carmel']

stand.describe_restaurant()
stand.show_flavors()
