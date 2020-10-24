"""
Make a class called User.
"""


class User:
    """Store user's inforamtion"""

    def __init__(self, first_name, last_name, age, height, weight):
        """Initialize first_name, last_name, age, height, weight"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.height = height
        self.weight = weight

    def describe_user(self):
        """Describe user"""
        print(f"\nThis is {self.first_name} {self.last_name}.")
        print(f"\tAge: {self.age}")
        print(f"\tHeight: {self.height} cm")
        print(f"\tWeight: {self.weight} kg")

    def greet_user(self):
        """Simple greet a user"""
        print(f"\nHi, {self.first_name}!\n")


# Create three instances
user = User('damian', 'ziolkowski', 25, 170, 72)
user.describe_user()
user.greet_user()
user2 = User('magda', 'czonstke', 25, 172, 50)
user2.describe_user()
user2.greet_user()
user3 = User('adam', 'nowak', 34, 150, 89)
user3.describe_user()
user3.greet_user()
