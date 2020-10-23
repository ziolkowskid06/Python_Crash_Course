"""
A buffet-style restaurant offers only five basic foods.
Think of five simple foods, and store them in a tuple.
"""

foods = ('chicken', 'noodles', 'egg', 'pawns', 'duck')
# Print menu
print("Menu:")
for food in foods:
    print(f"\t{food}")
# Rewrite new menu
foods = ('burrito', 'hamburger', 'tortilla', 'soup', 'pizza')
print("\nNew menu:")
for food in foods:
    print(f"\t{food}")
