"""
You just found out that your new dinner table won’t arrive in time for the dinner,
and you have space for only two guests.
"""

# Invite all peaple to the dinner.
guest_list = ['mary jane', 'elizabeth hurtley', 'salma hayek']
print(f'{guest_list[0].title()}, please come to my dinner!')
print(f'\n{guest_list[1].title()}, please come to my dinner!')
print(f'\n{guest_list[2].title()}, please come to my dinner!')
print('\n')
# Tell, you have bigger table for next three people
print("Ladies, I found bigger table. Let's invite three more people!!")
# Invite all the people.
guest_list.insert(0, 'demi moore')
guest_list.insert(2, 'penelope cruz')
guest_list.append('kate winslet')
print('\n')
print(f'\n{guest_list[0].title()}, please come to my dinner!')
print(f'\n{guest_list[1].title()}, please come to my dinner!')
print(f'\n{guest_list[2].title()}, please come to my dinner!')
print(f'\n{guest_list[3].title()}, please come to my dinner!')
print(f'\n{guest_list[4].title()}, please come to my dinner!')
print(f'\n{guest_list[5].title()}, please come to my dinner!')
# Tell, that the table didn't arrive on timme.
print('\n')
print("\nLadies, I sorry but the table didn't arrive on time.")
print("Hence, I can invite only two people for dinner.")
print('\n')
# Remove peapole from the list.
last_guest = guest_list.pop()
print(f"\n{last_guest.title()}, sorry but you can't come to my dinner.")
last_guest = guest_list.pop()
print(f"\n{last_guest.title()}, sorry but you can't come to my dinner.")
last_guest = guest_list.pop()
print(f"\n{last_guest.title()}, sorry but you can't come to my dinner.")
last_guest = guest_list.pop()
print(f"\n{last_guest.title()}, sorry but you can't come to my dinner.")
# Let the rest people know, they're still invited.
print('\n')
print(f'\n{guest_list[0].title()} you are still on my list, please come to my dinner!')
print(f'\n{guest_list[1].title()} you are still on my list, please come to my dinner!')
# Clean and check the empty list
del guest_list[0]
del guest_list[0]
print('\n')
print(guest_list)
