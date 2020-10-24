"""
Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed.
"""


def show_messages(messages):
    """Print a series of messages."""
    print("Showing following messages:")
    for message in messages:
        print(f"\t- {message}")


def send_messages(messages, sent_messages):
    """Print each message and move to a new list."""
    print("\nSending following messages:")
    while messages:
        text = messages.pop()
        print(f"\t- {text}")
        sent_messages.append(text)


messages = ['How are you?', 'Are you ok?', 'What time is it?']
show_messages(messages)
sent_messages = []
send_messages(messages, sent_messages)
# Check lists
print("\nCheck if 'message' list is empty:")
print(f"\tmessages: \n\t\t{messages}")
print(f"\tsent_messages: \n\t\t{sent_messages}")
