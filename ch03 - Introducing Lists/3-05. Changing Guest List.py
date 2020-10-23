"""
You just heard that one of your guests can’t make the dinner,
so you need to send out a new set of invitations.
You’ll have to think of someone else to invite.
"""

# Invite all peaple to the dinner.
guest_list = ['mary jane', 'elizabeth hurtley', 'salma hayek']
print(f'{guest_list[0].title()}, please come to my dinner!')
print(f'\n{guest_list[1].title()}, please come to my dinner!')
print(f'\n{guest_list[2].title()}, please come to my dinner!')
print('\n')
print(f"\nSorry, {guest_list[1].title()} can't make it to dinner.")
# Invite demi moore instead.
del(guest_list[1])
guest_list.insert(1, 'demi moore')
# Print all invitation again.
print('\n')
print(f'\n{guest_list[0].title()}, please come to my dinner!')
print(f'\n{guest_list[1].title()}, please come to my dinner!')
print(f'\n{guest_list[2].title()}, please come to my dinner!')
