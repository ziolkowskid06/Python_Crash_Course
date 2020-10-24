"""
Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
"""


def build_profile(first, last, **user_info):
    """Create a dictionry describing you."""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info


user_profile = build_profile('damian', 'ziolkowski',
                             location='ediburgh',
                             field='mechanics',
                             hobby='programming',
                             food='pizza')
print(user_profile)
