"""
Make a list of the first 10 cubes and print out the value of each cube.
"""

ten_cubes = []
for number in range(10):
    print(number**3)
    ten_cubes.append(number**3)
print(f"\n{ten_cubes}")
