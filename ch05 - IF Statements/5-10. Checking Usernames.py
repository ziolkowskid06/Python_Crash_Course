"""
Create a program that simulates how websites ensure that everyone has a unique username.
"""

current_names = ['anNA', 'EmmA', 'eliZabeTh', 'koRtney', 'jorDan', 'EVA', 'patricia']
new_users = ['rachel', 'samantha', 'EMMA', 'clementine', 'kendra', 'evA']
copy_current_names = [name.title() for name in current_names]
copy_new_users = [name.title() for name in new_users]
for new_user in copy_new_users:
    if new_user in copy_current_names:
        print(f"'{new_user}' is occupied! Please enter a new username.")
    else:
        print(f"'{new_user}' is available!")
