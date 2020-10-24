"""
Load a .txt file and print all lines in three different ways.
"""

filename = 'learning_python.txt'

print("\n--> Reading in the entire file:")
with open(filename) as f:
    content = f.read()
print(content)

print("\n--> Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--> Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())
