from decimal import Decimal


def at_least_one(chance, attempts):
    """
    Returns the chance to get at least one success on a number of attempts.
    """
    if chance > 1:
        chance = 1

    return Decimal(1 - (1 - chance) ** attempts)