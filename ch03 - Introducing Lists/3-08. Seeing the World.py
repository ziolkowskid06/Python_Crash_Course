"""
Think of at least five places in the world you’d like to visit.
"""

# Original list
places = ['roma', 'florence', 'london', 'aberdeen', 'glasgow', 'edinburgh', 'manchester']
print(places)
# Print your list in alphabetical order without modifying the actual list
print(sorted(places))
# Show that your list is still in its original order
print(places)
# Print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(places, reverse=True))
# Show that your list is still in its original order by printing it again.
print(places)
# Change the order of your list.
# Print the list to show that its order has changed
places.reverse()
print(places)
# Change the order of your list again.
# Print the list to show it’s back to its original order.
places.reverse()
print(places)
# Change your list so it’s stored in alphabetical order.
# Print the list to show that its order has been changed.
places.sort()
print(places)
# Change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.
places.sort(reverse=True)
print(places)
