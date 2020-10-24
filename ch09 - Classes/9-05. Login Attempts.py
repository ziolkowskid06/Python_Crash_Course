"""
Start with your program from Exercise 9-3.
"""


class User:
    """Store user's inforamtion"""

    def __init__(self, first_name, last_name):
        """Initialize first_name, last_name"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0

    def increment_login_attempts(self):
        """Increment login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0"""
        self.login_attempts = 0

    def describe_user(self):
        """Describe user"""
        print(f"\nThis is {self.first_name} {self.last_name}.")
        print(f"\tLogin attempts :{self.login_attempts}")

    def greet_user(self):
        """Simple greet a user"""
        print(f"\nHi, {self.first_name}!\n")


# Increment login_attempt 4 times and reset
user = User('damian', 'ziolkowski')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.describe_user()
user.reset_login_attempts()
user.describe_user()
