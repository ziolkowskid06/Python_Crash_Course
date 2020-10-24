"""
Save and load a file in the json format.
"""

"""
write: favorite_number_write.py
import json
"""

number = input("What's your favorite number? ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("Number is saved!")


"""
write: favorite_number_read.py
import json
"""

with open('favorite_number.json') as f:
    number = json.load(f)

print(f"Number loaded! It is {number}")
