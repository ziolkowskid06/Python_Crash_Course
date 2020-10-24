# Import randint function (random number in the range)
from random import randint


class Die:
    """
    Create a die of a different number of sides.
    Roll this dice.
    """

    def __init__(self, sides=6):
        """Initialize number of sides and rolls"""
        self.sides = sides
        self.rolls = 10

    def roll_die(self):
        """Roll a die"""
        print(f"\nThis is {self.sides} sides die.")
        print(f"Let's roll the dice {self.rolls} times!")
        for roll in range(1, self.rolls+1):
            print(f"\tRoll no. {roll} -> {randint(1, self.sides)}")


# For 6 sides die
my_dice = Die()
my_dice.roll_die()
# For 10 sides die
my_dice = Die(10)
my_dice.roll_die()
# For 20 sides die
my_dice = Die(20)
my_dice.roll_die()
