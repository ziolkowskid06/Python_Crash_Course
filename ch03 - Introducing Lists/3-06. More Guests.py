"""
You just found a bigger dinner table, so now more space is available.
Think of three more guests to invite to dinner.
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
