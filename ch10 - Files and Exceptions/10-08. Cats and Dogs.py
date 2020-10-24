"""
Print message when the file is missed.
"""

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                print(f"\t- {line.title()}")
    except FileNotFoundError:
        print("File missed!\n")
