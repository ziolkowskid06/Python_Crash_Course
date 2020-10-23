"""
Write two for loops to print each list of foods.
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("List of my food:")
for food in my_foods:
    print(f"\t{food}")
print("\nMy friend's list of food:")
for food in friend_foods:
    print(f"\t{food}")
