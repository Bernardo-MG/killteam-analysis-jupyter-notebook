from scripts.probability import at_least_one


def chance_to_hit(ballistics):
    """
    Gets the chance to hit.
    """
    range = 6 - (ballistics - 1)
    if range < 0:
        range = 0

    # chance to hit
    chance = (range / 6) * 100
    if chance > 100:
        chance = 100

    return str(chance)


def chance_to_wound(strength, toughness):
    """
    Gets the chance to hit.
    """
    if strength / toughness >= 2:
        # Doubles toughness
        roll = 2
    elif strength > toughness:
        # Greater than strength
        roll = 3
    elif strength == toughness:
        # Equal than strength
        roll = 4
    elif strength < toughness:
        # Lower than strength
        roll = 5
    elif toughness / strength >= 2:
        # Half than strength
        roll = 6
    else:
        roll = 7

    # Chance to wound
    chance = ((6 - (roll - 1)) / 6) * 100
    if chance > 100:
        chance = 100

    return str(chance)


def chance_to_fail_armour(ap, armour):
    """
    Gets the chance to pass the target armour.
    """
    roll = armour - ap

    # Chance to pass armour
    chance = ((6 - (roll - 1)) / 6)
    # Chance to fail armour
    chance = (1 - chance) * 100

    return str(chance)


def chance_to_damage(to_hit, to_wound, to_fail_armor):
    """
    Gets the chance to damage.
    """
    chance = (to_hit / 100) * (to_wound / 100) * (to_fail_armor / 100) * 100

    return str(chance)


def chance_to_damage_at_least_once(to_damage, attacks):
    """
    Gets the chance to damage in at least one attack.
    """
    return at_least_one(to_damage / 100, attacks) * 100
