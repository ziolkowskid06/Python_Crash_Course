"""
Make a list of people who should take the favorite languages poll.
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['samantha', 'phil', 'jen', 'salma', 'edward', 'eva', 'sarah']
for friend in friends:
    print(f'Hi {friend.title()}!')
    if friend not in favorite_languages.keys():
        print('\tYou should take the poll.')
    else:
        print('\tThank you for respond.')
