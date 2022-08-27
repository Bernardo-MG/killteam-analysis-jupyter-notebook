import re
import math

dice_regex = "[0-9]*d([0-9])+"

def average_dice_value(dice):
    """
    Returns the average value of a dice roll.
    """
    sides = re.search(dice_regex, dice)
    if sides:
        sides = sides.group(1)
        sides = int(sides)
        average = str(math.ceil(sides/2))
    else:
        average = dice

    return average
