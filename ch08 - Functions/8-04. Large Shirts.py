"""
Modify the make_shirt() function so that shirts are large by default with a message that reads, I love Python.
"""


def make_shirt(size='L', text='I love Python.'):
    """Provide the sieze and the text that should be printed on shirt."""
    print(f"You chose '{size}' size of the shirt.")
    print(f"The text printed on it is:\n\t'{text}'")


make_shirt()
