"""
Silent pass when file is missed.
"""

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        for line in lines:
            line = line.strip()
            print(f"\t- {line.title()}")
