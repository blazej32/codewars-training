from math import floor


def beeramid(bonus, price):
    cans_left = floor(bonus / price)
    levels_built = 0
    for i in range(1, cans_left + 1):
        if cans_left >= (i ** 2):
            levels_built += 1
            cans_left -= (i ** 2)
        else:
            break
    return levels_built
