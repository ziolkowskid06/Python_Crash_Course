"""
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
"""


def make_shirt(size, text):
    """Provide the sieze and the text that should be printed on shirt."""
    print(f"You chose '{size}' size of the shirt.")
    print(f"The text printed on it is:\n\t'{text}'")


make_shirt("M", "I like Pizza!")
