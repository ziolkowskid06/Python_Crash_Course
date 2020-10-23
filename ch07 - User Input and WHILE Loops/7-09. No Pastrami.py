"""
Using the list sandwich_orders, make sure the sandwich 'pastrami' appears in the list at least three times.
"""

sandwich_orders = ['tuna', 'chicken', 'pastrami', 'salami', 'pastrami', 'cheese', 'pastrami']
finished_sandwiches = []
print("The deli has run out of 'pastrami'.")
# Remove pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    finished_sandwiches.append(sandwich_orders.pop())
# Print sandwiches
print(f"\nSandwiches finished:\n\t{finished_sandwiches}")
