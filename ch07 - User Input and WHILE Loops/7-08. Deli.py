"""
Make a list called sandwich_orders and fill it with the names of various sandwiches.
"""

sandwich_orders = ['tuna', 'chicken', 'salami', 'cheese']
finished_sandwiches = []
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)
print("\nFollowing sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"\t- {sandwich}")
