"""
Make a list containing a series of short text messages.
"""


def show_messages(messages):
    """Print a series of messages."""
    for message in messages:
        print(f"{message}")


messages = ['How are you?', 'Are you ok?', 'What time is it?']
show_messages(messages)
