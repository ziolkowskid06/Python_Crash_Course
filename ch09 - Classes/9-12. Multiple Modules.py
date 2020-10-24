"""
Store the User class in one module, and store the Privileges and Admin classes in a separate module.
"""

"""
create: user.py
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


"""
create: admin.py
# Import User class
from user import User
"""


class Admin(User):
    """ Add Admin option"""

    def __init__(self, first_name, last_name, age, height, weight):
        """
        Initialize attributes of mother class.
        Add Admin privileges.
        """
        super().__init__(first_name, last_name, age, height, weight)
        self.privileges = Privileges()


class Privileges:
    """Create privileges class"""

    def __init__(self):
        """Initialize privilige's attributes"""
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Show admin's privileges"""
        print("\nAdmin has following privileges:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")


"""
create: my_admin.py
# Import Admin class
from admin import Admin
"""

# Create instance of Admin and call its method
user_admin = Admin('Damina', 'Ziolkowski', 25, 170, 72)
user_admin.describe_user()
user_admin.privileges.show_privileges()
