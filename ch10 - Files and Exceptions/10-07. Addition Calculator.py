"""
Loop previous exercise
"""

while True:
    print("---- Enter 'q' to quit ----\n")
    try:
        x = input("Enter a number: ")
        if x == 'q':
            break
        x = int(x)
        y = input("Enter a number: ")
        if y == 'q':
            break
        y = int(y)
    except ValueError:
        print("Only numbers are accepted!\n")
    else:
        sum = x + y
        print(f"The sum is: {sum}\n")
